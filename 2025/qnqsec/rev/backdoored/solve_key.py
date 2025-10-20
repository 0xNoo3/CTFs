#!/usr/bin/env python3
import hashlib

# Constants read from 0xC0E0 (little-endian dwords)
const_bytes = bytes([
    0xcf,0x68,0x00,0x00, 0xb5,0xaa,0x00,0x00, 0x21,0x00,0x00,0x00, 0x37,0x62,0x00,0x00,
    0x0a,0x73,0x00,0x00, 0x51,0x24,0x00,0x00, 0xdb,0x84,0x00,0x00, 0x5d,0x1d,0x00,0x00,
    0xfa,0x95,0x00,0x00, 0x04,0x8b,0x00,0x00, 0x78,0x57,0x00,0x00, 0x46,0x95,0x00,0x00,
    0x06,0x86,0x00,0x00, 0xa3,0xd0,0x00,0x00, 0x37,0x62,0x00,0x00, 0xd4,0x11,0x00,0x00,
])

consts = [int.from_bytes(const_bytes[i:i+4], 'little') for i in range(0, len(const_bytes), 4)]

# Inversion of validate_key transform for each pair:
# target16 = ((int(first4hex,16) - 0x32) ^ 0x2e) & 0xffff
# So int(first4hex,16) must be:
# want = ((target16 ^ 0x2e) + 0x32) & 0xffff

target_prefixes = [f"{((c ^ 0x2e) + 0x32) & 0xffff:04x}" for c in consts]

# Search printable ASCII for 2-char strings whose sha256 hex starts with target_prefix
charset = [chr(x) for x in range(0x21, 0x7f)]  # '!'..'~' avoid space and control/NUL

pairs = ['??'] * 16
for idx, pref in enumerate(target_prefixes):
    found = None
    for a in charset:
        for b in charset:
            s = (a + b).encode('latin1')
            h = hashlib.sha256(s).hexdigest()
            if h.startswith(pref):
                found = a + b
                break
        if found:
            break
    if not found:
        # try include space
        for a in [chr(x) for x in range(0x20, 0x7f)]:
            for b in [chr(x) for x in range(0x20, 0x7f)]:
                s = (a + b).encode('latin1')
                h = hashlib.sha256(s).hexdigest()
                if h.startswith(pref):
                    found = a + b
                    break
            if found:
                break
    if not found:
        raise SystemExit(f"No pair found for index {idx} prefix {pref}")
    pairs[idx] = found
    print(f"[{idx:02d}] prefix {pref} -> {found!r}")

key = ''.join(pairs)
print('Recovered 32-char key:', key)
