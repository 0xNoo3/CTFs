#!/usr/bin/env python3
from z3 import *

# 1) The given 21 Unicode codepoints:
cipher = "幾湂潌蕔䩘桢豝詧䭡䝵敯䡨剱挧䍩硷穏罣㈡䨥贇"
obs = [ord(c) for c in cipher]
N = len(obs)          # 21
L = 2 * N             # 42 input bytes

# 2) Create Z3 BitVecs for each input byte, constrain to printable ASCII:
f = [BitVec(f"f{i}", 8) for i in range(L)]
s = Solver()
for b in f:
    s.add(b >= 0x20, b <= 0x7e)   # adjust if your flag uses other chars

# Precompute “high‑nibbles” helper:
def hi_nibble(bv):
    return LShR(bv, 4)   # yields 0..15

# 3) For each cipher position k, build the same equations the C code uses:
for k in range(N):
    # chunk starts at byte index p = 2*k
    p = 2*k
    C0 = f[p]
    C1 = f[p+1]

    # Sum of high‑nibbles of ALL bytes from p+1 to end:
    sum_rest = Sum([hi_nibble(f[j]) for j in range(p+1, L)])

    # uVar3 = (C0>>4)&0xf  + sum_rest
    H0_nib = hi_nibble(C0)
    uVar3 = H0_nib + sum_rest

    # Extract observed hi_byte and lo_byte from obs[k]:
    code = obs[k] - 0x1000
    hi_byte = (code >> 8) & 0xff
    lo_byte = code & 0xff

    # Constrain that the high‑nibbles match:
    s.add( (C0 & 0xf0) == (hi_byte  & 0xf0) )
    s.add( (C1 & 0xf0) == (lo_byte  & 0xf0) )

    # Low‑nibble equations:
    #   ((uVar3>>4)&0xf + L0) &0xf == hi_byte &0xf
    #   (uVar3 + L1) &0xf        == lo_byte &0xf
    L0 = C0 & 0x0f
    L1 = C1 & 0x0f
    s.add( ((LShR(uVar3, 4) + L0) & 0xf) == (hi_byte & 0x0f) )
    s.add( ((uVar3             + L1) & 0xf) == (lo_byte & 0x0f) )

# 4) Solve!
if s.check() == sat:
    m = s.model()
    flag = "".join(chr(m.evaluate(f[i]).as_long()) for i in range(L))
    print("Recovered input: ", flag)
else:
    print("No solution found.")
