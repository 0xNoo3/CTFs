#!/usr/bin/env python3
import time
from z3 import BitVec, BitVecVal, Solver, URem

# --- Challenge constants ---
PRIME       = 2147483647
BASE        = 256
KEY         = 0x42424242
WINDOW_SIZE = 5
EXPECTED    = {
    0:  1910641389,
    5:   978734675,
    10:  639015185,
    15:  434697744,
    20:  977939275
}

# --- Fix the seed for May 17 2025 (days_since_epoch % 7) ---
# I computed via Python: (datetime(2025,5,17) - epoch).days % 7 == 2
seed_week = 2

def try_length(FLAG_LEN):
    # Z3 vars
    M = [BitVec(f"M{i}", 64) for i in range(FLAG_LEN)]
    # invert time-based mutation
    pre = []
    for i, mbv in enumerate(M):
        off = (i * seed_week) % 256
        # pre[i] = (M[i] + (256 - off)) & 0xFF
        pre_i = (mbv + BitVecVal((256 - off) & 0xFF, 64)) & BitVecVal(0xFF, 64)
        pre.append(pre_i)

    s = Solver()
    # rolling-hash constraints
    for start, chk in EXPECTED.items():
        if start + WINDOW_SIZE > FLAG_LEN:
            return None
        h = BitVecVal(0, 64)
        for k in range(WINDOW_SIZE):
            h = URem(h * BitVecVal(BASE, 64), BitVecVal(PRIME, 64))
            h = URem(h + pre[start + k], BitVecVal(PRIME, 64))
        s.add(h == BitVecVal(chk, 64))

    # printable ASCII on the *mutated* bytes
    for mbv in M:
        s.add(mbv >= BitVecVal(32, 64), mbv <= BitVecVal(126, 64))

    if s.check().r != 1:
        return None

    m = s.model()
    mutated = [m[M[i]].as_long() for i in range(FLAG_LEN)]
    return mutated

def invert_all(mutated):
    n = len(mutated)
    # 1) undo time mutation
    pre_bytes = [(mutated[i] - ((i * seed_week) % 256)) & 0xFF for i in range(n)]
    # 2) undo cascade XOR
    tmp = pre_bytes.copy()
    for i in range(1, n):
        tmp[i] ^= (tmp[i-1] >> 3)
    # 3) undo per-char XOR with 0x13371337 rotating mask
    orig_perm = []
    seed_val = 0x1337_1337
    for i, v in enumerate(tmp):
        mask = (seed_val >> (i % 32)) & 0xFF
        orig_perm.append(v ^ mask)
    # 4) invert the fixed-key swaps
    orig = orig_perm.copy()
    swaps = [(i, (i * KEY) % n) for i in range(n)]
    for i, j in reversed(swaps):
        orig[i], orig[j] = orig[j], orig[i]
    return "".join(map(chr, orig))

# Sweep lengths 25..60
for L in range(25, 61):
    res = try_length(L)
    if res:
        flag = invert_all(res)
        print(f"✅ Found with length={L}: {flag}")
        break
else:
    print("❌ No solution in lengths 25–60.")
