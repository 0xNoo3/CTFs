from struct import pack, unpack

def u32(x): return x & 0xFFFFFFFF

# — rebuild the 27‑byte buffer from xmmword_2050 at 0 and xmmword_2060 at 11
hex2050 = "76332510663765351E60162D6F5E3802"
hex2060 = "0A7D5E0503615B4C4C00377633251066"

buf = bytearray(27)
for i in range(16):
    buf[i] = int(hex2050[2*i:2*i+2], 16)
for i in range(16):
    if 11+i < 27:
        buf[11+i] = int(hex2060[2*i:2*i+2], 16)

# — run the 25‑round SSE “mix” exactly as before to compute lane0
si   = [0x61,0x62,0x63,0x64]
v7   = [u32(0xFFFFFFFC)]*4
v5   = [0,0,0,0]

for _ in range(25):
    old = si[:]
    si = [u32(old[i] + v7[i]) for i in range(4)]
    # mul_epu32(old,old)
    p0 = old[0]*old[0]; p2 = old[2]*old[2]
    v10 = [u32(p0),u32(p0>>32),u32(p2),u32(p2>>32)]
    # srli_epi64(old,32)
    v11 = [old[1],0,old[3],0]
    p0 = v11[0]*v11[0]; p2 = v11[2]*v11[2]
    v11m = [u32(p0),u32(p0>>32),u32(p2),u32(p2>>32)]
    sh10 = [v10[0],v10[2],v10[0],v10[0]]
    sh11 = [v11m[0],v11m[2],v11m[0],v11m[0]]
    unpack = [sh10[0],sh11[0],sh10[1],sh11[1]]
    t = [u32(old[i]<<3) for i in range(4)]
    v5 = [u32(v5[i] + (t[i] ^ unpack[i])) for i in range(4)]

# horizontal adds: v12 = v5 + (v5 >> 64), then + (v12 >> 32)
temp1 = [v5[0]+v5[2], v5[1]+v5[3], v5[2], v5[3]]
temp2 = [temp1[0]+temp1[1],
         temp1[1]+temp1[2],
         temp1[2]+temp1[3],
         temp1[3]]
lane0 = u32(temp2[0])

# v13 = (-559038737) * lane0  modulo 2^32
v13 = u32(0xDEADBEEF * lane0)

# **THIS IS THE CRITICAL FIX**: reduce modulo 0x7FFFFFFF before seeding
seed = v13 % 0x7FFFFFFF

# now run the LCG→XOR over the 27‑byte buffer
a, b = 1103515245, 12345
v17 = seed
for i in range(27):
    v17 = (a*v17 + b) & 0x7FFFFFFF  # note mask to 31 bits
    buf[i] ^= (v17 >> 8) & 0xFF

print(buf.decode('ascii'))
