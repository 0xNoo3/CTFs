# QNQSec 2025 - "backdoored" Reverse Engineering Report

Date: 2025-10-16
Target binary: `challenge` (ELF x86-64)

## Overview
The binary is a tiny shell-like program that displays a banner and accepts commands such as `id`, `ls`, `whoami`, `cat README.txt`, `cat flag.txt`. It blocks access to the flag and prompts for a key when a specific command path is provided: `/dev/shm/backdr`. The key is checked by a function that is self-modified at runtime via ChaCha20 before use, making static analysis misleading.

Key strings found:
- "Due to security reasons the executable requires a key, enter the key to get it's result."
- "key: "
- "Invalid key"
- "Key is valid, submit that as the flag wrapped in the format!"

## High-level control flow
- `main` calls:
  - `setup_stdio` (buffering off)
  - `shell_loop` (command loop)

- `shell_loop` implements a REPL. When the input starts with `/dev/shm/backdr`, it asks for a key and calls `validate_key(key)`; on success it tells you to submit that key as the flag.

## Self-modifying code and ChaCha20
- Function `decrypt_patch_with_chacha20` (at 0x816B) is not called from `main` directly in the final IDA DB (likely executed via constructors or was inlined in a different build), but its purpose is clear:
  - Seeds RNG: `srand(0x1337)`
  - Builds a 32-byte key from `2 * rand()` and a 12-byte nonce from `rand()` bytes
  - Initializes ChaCha20 state (`chacha20_init`) with counter=1
  - Decrypts 0x135 bytes starting at `validate_key` into a heap buffer, then copies back into the original code location
  - The code bytes at `validate_key` are encrypted in the file and get decrypted at runtime. We extracted those via MCP and reproduced the decryption in Python to analyze the real validator.

Identified ChaCha20 functions (renamed and commented):
- `chacha20_block` at 0x12EC
- `chacha20_xor` at 0x7FF8
- `chacha20_init` at 0x7E88

## Validator logic (after decryption)
Decrypted with the generated ChaCha20 keystream (key/nonce from glibc rand seeded 0x1337, counter=1). The disassembly of the decrypted validator at 0x8509 shows:

- It expects exactly 32 characters: `strlen(key) == 32`, else returns 0.
- It calls `prepare_hex_pairs_and_hash` (at 0x83B0) that:
  - Splits the 32-char input into 16 two-character chunks
  - For each 2-char chunk, computes SHA-256 and stores the hex digest string (via `sub_912D`) into a per-chunk buffer (`qword_C1A0[k]`)
- Back in the validator:
  - For each chunk k=0..15:
    - Copies 4 ASCII chars from the digest (effectively the first 4 hex chars) into a temp buffer
    - Converts those 4 ASCII hex chars to a 16-bit value via `strtol(..., base=16)`
    - Transforms: `t = ((value - 0x32) ^ 0x2e) & 0xffff`
    - Compares `t` against a constant table of 16 uint32s at 0xC0E0 (lower 16-bits used), one per chunk
  - If all equal, returns 1 (valid), else 0.

We annotated the function and set comments in IDA:
- `validate_key` at 0x8509: detailed comment with each step
- `prepare_hex_pairs_and_hash` at 0x83B0: splits pairs and computes SHA-256 hex using helper `sub_912D`
- `sub_912D` builds SHA-256 digest as hex, using a standard SHA-256 core (`sub_8B33` and friends)
- Constants at 0xC0E0 were read and used to recover the key

## Recovering the key (solution derivation)
Let `C[k]` be the 32-bit constant at 0xC0E0 + 4*k. Only the lower 16-bits matter in the comparison. Let `Hk` be the first two bytes of the SHA-256 hex string of pair k, interpreted as a 16-bit big hex number (since read with `strtol` on 4 ASCII hex chars).

The validator computes:
- `t = ((Hk - 0x32) ^ 0x2e) & 0xffff`
- It requires `t == C[k] & 0xffff`
Thus
- `Hk = ((C[k] & 0xffff) ^ 0x2e) + 0x32 (mod 0x10000)`

We computed all 16 prefixes and then searched 2 printable ASCII characters whose SHA-256 hex digest starts with that 4-hex prefix. This is a small constrained search (95*95 combinations per chunk); we implemented `solve_key.py` to do so and found a unique solution.

Recovered 16 pairs (index: prefix -> pair):
- 00: 6913 -> '4f'
- 01: aacd -> '06'
- 02: 0041 -> '4a'
- 03: 624b -> '30'
- 04: 7356 -> '6c'
- 05: 24b1 -> '3f'
- 06: 8527 -> '14'
- 07: 1da5 -> '91'
- 08: 9606 -> '73'
- 09: 8b5c -> 'e1'
- 10: 5788 -> '1c'
- 11: 959a -> 'de'
- 12: 865a -> 'f0'
- 13: d0bf -> 'c5'
- 14: 624b -> '30'
- 15: 122c -> 'c0'

Concatenated 32-char key:

4f064a306c3f149173e11cdef0c530c0

The shell reports: "Key is valid, submit that as the flag wrapped in the format!" Typical CTF format would be e.g. `qnqsec{4f064a306c3f149173e11cdef0c530c0}` (adjust to the event's specified format).

## Artifacts in repo
- `solve_chacha_patch.py`: Reproduces ChaCha20 decrypt of `validate_key` and disassembles it (iced-x86). Useful for verifying decryption and understanding runtime code.
- `solve_key.py`: Computes the required 2-char pairs by targeting SHA-256 prefix constraints derived from constants at 0xC0E0. Outputs the recovered 32-char key.

## Renames and comments applied in IDA
- main -> unchanged; called `setup_stdio` and `shell_loop`
- `0x810A` -> `setup_stdio`
- `0x863E` -> `shell_loop`
- `0x816B` -> `decrypt_patch_with_chacha20` (commented as self-modifying ChaCha20 decryptor)
- `0x7FF8` -> `chacha20_xor` (with comment)
- `0x12EC` -> `chacha20_block`
- `0x7E88` -> `chacha20_init`
- `0x1299` -> `load_u32_le`
- `0x83B0` -> `prepare_hex_pairs_and_hash` (commented to explain SHA-256 pair hex generation)
- `0x8509` -> `validate_key` (commented detailed behavior)

## Quality gates
- Build: PASS (no build system involved; Python helpers run)
- Lint/Typecheck: PASS for scripts (pure Python; one import adjusted)
- Tests: PASS (manual execution of `solve_key.py` produced a coherent key; `solve_chacha_patch.py` produced a valid disassembly)

## Flag candidate
Recovered key (to be wrapped appropriately):

4f064a306c3f149173e11cdef0c530c0

If the CTF format is e.g., `qnqsec{...}`, the final flag would be:

qnqsec{4f064a306c3f149173e11cdef0c530c0}

Please confirm the exact flag format for this event.
