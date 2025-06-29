from sympy import prime
from functools import lru_cache

# Encrypted flag bytes
encrypted_flag = [
    0xEA, 0x09, 0x12, 0x47, 0x98, 0x2D, 0xDB, 0x17, 0xD5, 0xBE,
    0xE3, 0xDE, 0xCF, 0x62, 0xB3, 0xB2, 0x73, 0xAF, 0xE6,
    0xE1, 0xB5, 0x5F, 0xC3, 0x19, 0x0E, 0xFD, 0xE2
]

# Efficient Fibonacci using memoization
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Since fib(10000 + i) is huge, we only need the last byte for XOR
def fib_mod_256(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 256
    return a

flag = ""

for i in range(27):
    fib_key = fib_mod_256(10000 + i)
    prime_val = prime(500000 + i) % 256
    decrypted_char = encrypted_flag[i] ^ fib_key ^ prime_val
    flag += chr(decrypted_char)

print("Flag:", flag)
