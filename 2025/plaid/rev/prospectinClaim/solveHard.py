from z3 import *
from constraints import Constraints, input

score = BitVecVal(0, 8*4)
solver = Solver()

for constraint in Constraints:
    score = If(constraint, score + 1, score)

solver.add(UGT(score,0x118))

if solver.check() == sat:
    print(solver.model())