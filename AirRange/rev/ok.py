# Recompute with corrected overlap handling

# QWORD values
Q1 = bytes.fromhex('1509022c1e10073f')
Q2 = bytes.fromhex('3c21304c073a3723')
Q3 = bytes.fromhex('073a372356264611')
Q4 = bytes.fromhex('573931260b551b36')

# Build encrypted region of length 28:
enc = Q1 + Q2[:4] + Q3 + Q4

print("Encrypted bytes:", enc.hex())

key = b'secKey'

# Decrypt
flag = bytearray(len(enc))
for i, c in enumerate(enc):
    flag[i] = c ^ key[i % len(key)]

print("Decrypted:", flag.decode('ascii', errors='ignore'))
