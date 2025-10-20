#!/usr/bin/env python3
from __future__ import annotations
import ctypes
import struct
from dataclasses import dataclass

# Recreate glibc's rand() semantics for typical 32-bit RAND_MAX? Actually GNU uses 31-bit.
# But here they only use rand() % 256 then *2 or raw byte. In code: v2[i] = 2 * rand(); v1[j] = rand();
# That uses full rand() value truncated to byte. glibc rand() returns 31-bit value.
# However IDA decompile shows calling srand(0x1337) and then rand(); we can replicate using Python's ctypes and libc if available.

# We'll implement a minimal glibc rand with seed 0x1337 using the linear congruential generator used by glibc? Actually glibc uses a more complex algorithm.
# Simpler approach: use Python's ctypes to call libc srand/rand so we match exactly on this system.

libc = ctypes.CDLL(None)
libc.srand.argtypes = [ctypes.c_uint]
libc.rand.restype = ctypes.c_int


def gen_key_nonce():
    libc.srand(0x1337)
    key = bytearray(32)
    for i in range(32):
        key[i] = (libc.rand() * 2) & 0xFF
    nonce = bytearray(12)
    for j in range(12):
        nonce[j] = libc.rand() & 0xFF
    counter = 1
    return bytes(key), bytes(nonce), counter


def load_u32_le(b: bytes, off: int) -> int:
    return struct.unpack_from('<I', b, off)[0]


def rotl32(x: int, r: int) -> int:
    x &= 0xFFFFFFFF
    return ((x << r) | (x >> (32 - r))) & 0xFFFFFFFF


def chacha20_block(state: list[int]) -> bytes:
    # state: 16 x 32-bit
    x = state.copy()
    # 10 double rounds
    for _ in range(10):
        # column rounds
        # a0,a4,a8,a12
        x[0] = (x[0] + x[4]) & 0xFFFFFFFF
        x[12] ^= x[0]; x[12] = rotl32(x[12], 16)
        x[8] = (x[8] + x[12]) & 0xFFFFFFFF
        x[4] ^= x[8]; x[4] = rotl32(x[4], 12)
        x[0] = (x[0] + x[4]) & 0xFFFFFFFF
        x[12] ^= x[0]; x[12] = rotl32(x[12], 8)
        x[8] = (x[8] + x[12]) & 0xFFFFFFFF
        x[4] ^= x[8]; x[4] = rotl32(x[4], 7)
        # a1,a5,a9,a13
        x[1] = (x[1] + x[5]) & 0xFFFFFFFF
        x[13] ^= x[1]; x[13] = rotl32(x[13], 16)
        x[9] = (x[9] + x[13]) & 0xFFFFFFFF
        x[5] ^= x[9]; x[5] = rotl32(x[5], 12)
        x[1] = (x[1] + x[5]) & 0xFFFFFFFF
        x[13] ^= x[1]; x[13] = rotl32(x[13], 8)
        x[9] = (x[9] + x[13]) & 0xFFFFFFFF
        x[5] ^= x[9]; x[5] = rotl32(x[5], 7)
        # a2,a6,a10,a14
        x[2] = (x[2] + x[6]) & 0xFFFFFFFF
        x[14] ^= x[2]; x[14] = rotl32(x[14], 16)
        x[10] = (x[10] + x[14]) & 0xFFFFFFFF
        x[6] ^= x[10]; x[6] = rotl32(x[6], 12)
        x[2] = (x[2] + x[6]) & 0xFFFFFFFF
        x[14] ^= x[2]; x[14] = rotl32(x[14], 8)
        x[10] = (x[10] + x[14]) & 0xFFFFFFFF
        x[6] ^= x[10]; x[6] = rotl32(x[6], 7)
        # a3,a7,a11,a15
        x[3] = (x[3] + x[7]) & 0xFFFFFFFF
        x[15] ^= x[3]; x[15] = rotl32(x[15], 16)
        x[11] = (x[11] + x[15]) & 0xFFFFFFFF
        x[7] ^= x[11]; x[7] = rotl32(x[7], 12)
        x[3] = (x[3] + x[7]) & 0xFFFFFFFF
        x[15] ^= x[3]; x[15] = rotl32(x[15], 8)
        x[11] = (x[11] + x[15]) & 0xFFFFFFFF
        x[7] ^= x[11]; x[7] = rotl32(x[7], 7)
        # diagonal rounds
        # a0,a5,a10,a15
        x[0] = (x[0] + x[5]) & 0xFFFFFFFF
        x[15] ^= x[0]; x[15] = rotl32(x[15], 16)
        x[10] = (x[10] + x[15]) & 0xFFFFFFFF
        x[5] ^= x[10]; x[5] = rotl32(x[5], 12)
        x[0] = (x[0] + x[5]) & 0xFFFFFFFF
        x[15] ^= x[0]; x[15] = rotl32(x[15], 8)
        x[10] = (x[10] + x[15]) & 0xFFFFFFFF
        x[5] ^= x[10]; x[5] = rotl32(x[5], 7)
        # a1,a6,a11,a12
        x[1] = (x[1] + x[6]) & 0xFFFFFFFF
        x[12] ^= x[1]; x[12] = rotl32(x[12], 16)
        x[11] = (x[11] + x[12]) & 0xFFFFFFFF
        x[6] ^= x[11]; x[6] = rotl32(x[6], 12)
        x[1] = (x[1] + x[6]) & 0xFFFFFFFF
        x[12] ^= x[1]; x[12] = rotl32(x[12], 8)
        x[11] = (x[11] + x[12]) & 0xFFFFFFFF
        x[6] ^= x[11]; x[6] = rotl32(x[6], 7)
        # a2,a7,a8,a13
        x[2] = (x[2] + x[7]) & 0xFFFFFFFF
        x[13] ^= x[2]; x[13] = rotl32(x[13], 16)
        x[8] = (x[8] + x[13]) & 0xFFFFFFFF
        x[7] ^= x[8]; x[7] = rotl32(x[7], 12)
        x[2] = (x[2] + x[7]) & 0xFFFFFFFF
        x[13] ^= x[2]; x[13] = rotl32(x[13], 8)
        x[8] = (x[8] + x[13]) & 0xFFFFFFFF
        x[7] ^= x[8]; x[7] = rotl32(x[7], 7)
        # a3,a4,a9,a14
        x[3] = (x[3] + x[4]) & 0xFFFFFFFF
        x[14] ^= x[3]; x[14] = rotl32(x[14], 16)
        x[9] = (x[9] + x[14]) & 0xFFFFFFFF
        x[4] ^= x[9]; x[4] = rotl32(x[4], 12)
        x[3] = (x[3] + x[4]) & 0xFFFFFFFF
        x[14] ^= x[3]; x[14] = rotl32(x[14], 8)
        x[9] = (x[9] + x[14]) & 0xFFFFFFFF
        x[4] ^= x[9]; x[4] = rotl32(x[4], 7)
    out = [(x[i] + state[i]) & 0xFFFFFFFF for i in range(16)]
    return struct.pack('<16I', *out)


def chacha20_xor(key: bytes, nonce: bytes, counter: int, data: bytes) -> bytes:
    const = b'expand 32-byte k'
    state = [
        load_u32_le(const, 0),
        load_u32_le(const, 4),
        load_u32_le(const, 8),
        load_u32_le(const, 12),
        *(load_u32_le(key, i) for i in range(0, 32, 4)),
        counter,
        load_u32_le(nonce, 0),
        load_u32_le(nonce, 4),
        load_u32_le(nonce, 8),
    ]
    # ensure length 16
    assert len(state) == 16
    out = bytearray(len(data))
    pos = 0
    while pos < len(data):
        block = chacha20_block(state)
        n = min(64, len(data) - pos)
        for i in range(n):
            out[pos + i] = data[pos + i] ^ block[i]
        # increment counter (state[12]) like in code
        state[12] = (state[12] + 1) & 0xFFFFFFFF
        if state[12] == 0:
            state[13] = (state[13] + 1) & 0xFFFFFFFF
            if state[13] == 0:
                raise AssertionError('ctx->state[13] != 0')
        pos += n
    return bytes(out)


PATCH_ADDR = 0x8509
PATCH_SIZE = 0x135
# Extract the bytes from the provided dump earlier? We'll paste hex array captured via MCP.
patch_bytes = bytes([
    0x84,0x6a,0x01,0x53,0xdb,0xaa,0x73,0x29,0xe0,0x5d,0x6c,0xa4,0x54,0xa7,0xff,0x6b,
    0x88,0x7e,0xf1,0xcd,0xde,0xa1,0x81,0x92,0xe7,0x72,0xb0,0x5f,0x39,0x02,0x29,0xfa,
    0xda,0x6f,0xea,0x4e,0x15,0xe0,0x69,0xe7,0xb1,0xe8,0xaf,0x28,0xd0,0x93,0x99,0x73,
    0xcd,0x2a,0x22,0x6a,0xae,0xf7,0xa2,0xc0,0x9c,0x7c,0xd3,0xf1,0xba,0x98,0x17,0xb5,
    0xc2,0x5e,0xb4,0x4f,0x42,0x97,0x12,0xd2,0x78,0xaa,0x28,0x30,0xd0,0x67,0xab,0x4a,
    0x1f,0xc7,0x8a,0x33,0x53,0x1c,0x42,0x56,0x25,0x02,0xf3,0x29,0xbc,0xfd,0x20,0x11,
    0x0d,0xb7,0x28,0x7a,0x38,0x53,0xa1,0xbf,0xfa,0xd1,0xc6,0x7e,0xc7,0xa8,0x96,0xb6,
    0xc1,0x0d,0x90,0x54,0xea,0x1c,0xd5,0xb2,0x33,0x64,0xe1,0x53,0xd3,0xe8,0x05,0x21,
    0x28,0x2c,0xba,0x28,0xec,0x9a,0xea,0xf3,0x7b,0x9a,0x3c,0xfa,0x7c,0x3e,0x00,0x34,
    0xba,0xd1,0xe9,0xe2,0xeb,0x3c,0x0a,0x22,0xe1,0xf1,0x05,0x4e,0xa0,0xb1,0x02,0x01,
    0xa2,0x60,0x70,0xb1,0x60,0xae,0x54,0x4d,0x0b,0x18,0xbb,0xda,0x13,0xb5,0xd3,0x12,
    0x5c,0x09,0xce,0xe6,0x41,0x59,0xc1,0x85,0x9d,0x14,0x86,0xc4,0x26,0x89,0x64,0x05,
    0xee,0x31,0x06,0xba,0x92,0x72,0x94,0x16,0x9d,0x59,0xe6,0x29,0x53,0xa7,0xee,0x51,
    0xe5,0xe3,0xb4,0x92,0xc5,0xac,0x46,0xbf,0x95,0xaa,0x20,0xa1,0x15,0x5f,0x73,0xb0,
    0x29,0x37,0xc0,0x08,0x20,0x84,0xa3,0xbb,0xa9,0xb6,0xc5,0x4d,0x6b,0x54,0xac,0x10,
    0xb4,0xbc,0xa7,0x93,0x2d,0x21,0xd3,0x21,0x24,0x0b,0xfb,0x68,0xa7,0x2f,0x79,0xd9,
    0x6f,0x2c,0x42,0xdf,0x42,0x20,0x58,0xf0,0x77,0xa2,0xe8,0xd5,0xc8,0xd1,0xb0,0x44,
    0x97,0x67,0x4c,0xe0,0x1a,0x32,0x8d,0xbe,0xb2,0xc1,0x55,0xe9,0xc2,0xe7,0x23,0x07,
    0xf0,0xfa,0xf6,0x00,0x88,0xc8,0x04,0x70,0x6b,0xa7,0x85,0x17,0xee,0xb0,0x2d,0x75,
    0x11,0xb3,0x57,0x64,0xb2
])


def main():
    key, nonce, counter = gen_key_nonce()
    plain = chacha20_xor(key, nonce, counter, patch_bytes)
    print('Decrypted length:', len(plain))
    # Disassemble x86-64
    try:
        from iced_x86 import Decoder, DecoderOptions, Formatter, FormatterSyntax
        base = PATCH_ADDR
        dec = Decoder(64, plain, ip=base, options=DecoderOptions.NONE)
        fmt = Formatter(FormatterSyntax.NASM)
        for insn in dec:
            s = fmt.format(insn)
            print(f"0x{insn.ip:x}:\t{s}")
    except Exception as e:
        print('Disasm failed:', e)
        print(plain.hex())


if __name__ == '__main__':
    main()
