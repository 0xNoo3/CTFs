# Python code to solve the CTF challenge
# Constants from the assembly
initial_v71 = 0xDFB432BC61353FB0
C = 0xCFA8C7711A026A35
D = 0x453E9537620FF1E3

# Target bytes as given (first 38 bytes)
target_bytes = [
    0x3A, 0x77, 0x2C, 0xA8, 0x0A, 0x82, 0xD2, 0x7F, 0x55, 0x11,
    0x40, 0xB6, 0x62, 0x64, 0x8C, 0x39, 0x4E, 0xDE, 0xCB, 0x8B,
    0x91, 0x49, 0x60, 0xA8, 0xF1, 0x2F, 0xBD, 0xE5, 0xE0, 0x7B,
    0xDB, 0xDA, 0x7B, 0xD3, 0x33, 0x04, 0x28, 0x9E
]

v71 = initial_v71
flag_bytes = []

# Iterate 38 times
for i in range(38):
    # Update v71 with 64-bit overflow
    v71 = (C - D * v71) & ((1 << 64) - 1)
    # Compute key: bits 21-28 (shift right 21, mask 8 bits)
    key = (v71 >> 21) & 0xFF
    # Derive input byte
    input_byte = target_bytes[i] ^ key
    flag_bytes.append(input_byte)

# Convert to ASCII
flag = bytes(flag_bytes).decode('ascii', errors='replace')
print("Flag:", flag)
