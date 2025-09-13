import struct

raw_vals = [
    0x3535556c4e62315b,
    0x4063312478402b40,
    0x4041432e4077246a,
    0x2d40356140333864,
]
final_val = 0x5e31773b6523352d

mem = bytearray(39)
for i, v in enumerate(raw_vals):
    mem[i * 8:i * 8 + 8] = struct.pack("<Q", v)
mem[31:39] = struct.pack("<Q", final_val)

data = list(mem)

def transform(n):
    if n == 9:
        r = -20
    else:
        t = n ^ 9
        r = -5
        if t != 17:
            z = ((t - 8) & 0xFF) ^ 9
            a = (z + 0xBF) & 0xFF
            if a < 26:
                u = ((z - 0x34) % 26) + 0x37
                v = (u ^ 9) - 3
                r = v if v != 0 else 1
            elif ((z + 0x9F) & 0xFF) < 26:
                u = ((z - 0x54) % 26) + 0x57
                r = (u ^ 9) - 3
            else:
                m = z - 10
                r = -2
                if m != 9:
                    v = (m ^ 9) - 3
                    r = v if v != 0 else 1
    if r < -128 or r > 127:
        r = (r + 256) & 0xFF
        if r >= 128:
            r -= 256
    return r

target_vals = [(b if b < 128 else b - 256) for b in data]

results = []
for i, tgt in enumerate(target_vals):
    matches = [c for c in range(256) if transform(c) == tgt]
    results.append(matches)
    print(i, tgt, len(matches), matches[:10])

decoded = "".join(chr(cands[0]) for cands in results)
print(decoded)
