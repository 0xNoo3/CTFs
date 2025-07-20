#!/usr/bin/env python3
import lief
import struct

# --- 1) Parse the ELF and grab .rodata ---
binary = lief.parse("pacman")
ro = next((s for s in binary.sections if s.name == ".rodata"), None)
if ro is None:
    raise RuntimeError("Could not find .rodata section")

ro_base = ro.virtual_address
ro_data = bytes(ro.content)

def read_qword(at_addr):
    """
    Read an 8‑byte little‑endian QWORD from .rodata at virtual address `at_addr`.
    """
    off = at_addr - ro_base
    return struct.unpack_from("<Q", ro_data, off)[0]

# --- 2) Extract the 4 round‑keys (8 bytes each) at 0x402020 … 0x402037 ---
keys = [read_qword(0x402020 + 8*i) for i in range(4)]
print("[*] Round‑keys:")
for i,k in enumerate(keys):
    print(f"    K{i}: 0x{k:016x}")

# --- 3) Extract the 32‑byte encrypted flag at 0x402040 … 0x40205f ---
enc_off = 0x402040 - ro_base
enc = ro_data[enc_off : enc_off + 32]
print(f"[*] Encrypted blob: {enc.hex()}")

# --- 4) Implement the same round function (from 0x4011f6) ---
MASK64 = (1<<64) - 1

def roundf(x, k):
    # x ^= k
    x = (x ^ k) & MASK64
    # rol x by 13
    r = ((x << 13) & MASK64) | (x >> (64-13))
    # ((x << 5) - x) ^ r
    return (((x << 5) & MASK64) - x) ^ r

# --- 5) Feistel‑style decryption (reverse key order) ---
def decrypt_block(block16):
    L, R = struct.unpack("<QQ", block16)
    for k in reversed(keys):
        newL = (roundf(L, k) ^ R) & MASK64
        newR = L & MASK64
        L, R = newL, newR
    return struct.pack("<QQ", L, R)

# --- 6) Decrypt both halves and print the flag ---
plain = decrypt_block(enc[:16]) + decrypt_block(enc[16:])
print("[*] Decrypted flag:", plain.decode("ascii"))
