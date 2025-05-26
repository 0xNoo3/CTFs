import math

# Cipher text from the challenge (z-base-32 encoded)
cipher = "m7xzr7muqtxsr3m8pfzf6h5ep738ez5ncftss7d1cftskz49qj4zg7n9cizgez5upbzzr7n9cjosg45wqjosg3mu"

# z-base-32 alphabet
alphabet = "ybndrfg8ejkmcpqxot1uwisza345h769"
rev = {c: i for i, c in enumerate(alphabet)}

# Convert each character to its 5-bit representation
bits = "".join(format(rev[ch], '05b') for ch in cipher)

# Group into bytes (8 bits)
decoded = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits) // 8 * 8, 8))

# Display the decoded plaintext
password  = decoded.decode()
print(password)
