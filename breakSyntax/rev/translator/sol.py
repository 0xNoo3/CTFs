import numpy as np

cipher = "幾湂潌蕔䩘桢豝詧䭡䝵敯䡨剱挧䍩硷穏罣㈡䨥贇"

# Convert ciphertext characters to raw bytes (hi_byte, low_byte)
raw = [ord(c) - 0x1000 for c in cipher]
hi_bytes = [(v >> 8) & 0xFF for v in raw]
low_bytes = [v & 0xFF for v in raw]

# Derive high nibble sequence for all input bytes
num_pairs = len(raw)
high_nibs = []
for hb, lb in zip(hi_bytes, low_bytes):
    high_nibs.append(hb >> 4)
    high_nibs.append(lb >> 4)

# Compute suffix sums of high_nibs
suffix_sums = [sum(high_nibs[i+1:]) for i in range(len(high_nibs))]

# Recover full input bytes
recovered = []
for i in range(num_pairs):
    idx0 = 2 * i
    idx1 = idx0 + 1
    U3 = high_nibs[idx0] + suffix_sums[idx0]
    
    hi_byte = hi_bytes[i]
    lo_byte = low_bytes[i]
    
    # Solve for low nibbles
    x = ((hi_byte & 0xF) - ((U3 >> 4) & 0xF)) & 0xF
    y = ((lo_byte & 0xF) - (U3 & 0xF)) & 0xF
    
    b0 = (high_nibs[idx0] << 4) | x
    b1 = (high_nibs[idx1] << 4) | y
    recovered.extend([b0, b1])

flag = bytes(recovered).decode('utf-8')
print("Recovered flag:", flag)
