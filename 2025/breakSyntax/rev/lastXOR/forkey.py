#!/usr/bin/env python3
import sys

# Try to import Capstone; if missing, instruct how to install.
try:
    from capstone import Cs, CS_ARCH_X86, CS_MODE_64
except ImportError:
    print("Error: capstone module not found. Please install it with:")
    print("    pip install capstone")
    sys.exit(1)

# Configuration
KEY = 0x42       # the XOR key we found
BLOB_FILE = "blob.encrypted"

# Read the encrypted blob
with open(BLOB_FILE, "rb") as f:
    enc = f.read()
if len(enc) != 199:
    print(f"Warning: expected 199 bytes, got {len(enc)}")

# Decrypt
dec = bytes(b ^ KEY for b in enc)

# (Optional) write decrypted binary to disk for GDB loading
with open("blob.decrypted", "wb") as f:
    f.write(dec)

# 1) Hex dump
print("=== Hex dump of decrypted blob (199 bytes) ===")
for i in range(0, len(dec), 16):
    chunk = dec[i:i+16]
    hex_bytes = " ".join(f"{b:02x}" for b in chunk)
    print(f"{i:04x}: {hex_bytes}")

# 2) Capstone disassembly
print("\n=== Disassembly of decrypted blob ===")
md = Cs(CS_ARCH_X86, CS_MODE_64)
for insn in md.disasm(dec, 0x0):
    print(f"0x{insn.address:04x}:\t{insn.mnemonic}\t{insn.op_str}")
