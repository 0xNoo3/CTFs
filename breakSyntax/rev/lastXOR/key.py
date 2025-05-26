#!/usr/bin/env python3
from pathlib import Path

blob = Path('blob.encrypted').read_bytes()

def looks_like_code(data: bytes) -> bool:
    # Check for common x86-64 function prologue: 55 48 89 e5
    return data.startswith(b'\x55\x48\x89\xe5')

candidates = []
for k in range(256):
    # XOR the first few bytes with k
    dec = bytes(b ^ k for b in blob[:4])
    if looks_like_code(dec):
        candidates.append(k)

if not candidates:
    print("No key found—try inspecting more bytes or adjusting the pattern.")
else:
    print("Possible key byte(s):")
    for k in candidates:
        print(f"  0x{k:02x}")
