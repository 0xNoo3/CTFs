from z3 import *
from constraints import conds, bitvecs

# solver = Solver()
optimize = Optimize()

for single in conds:
    # solver.add(single)
    optimize.add_soft(single)

# print(solver.check())
print(optimize.check())
flag = ""
if optimize.check() == sat:
    # print(optimize.model())
    model = optimize.model()
    for index, value in bitvecs.items():
        flag += chr(model[value].as_long()) # as long required to convert it from bitVec to integer
    print(flag)

# for bitvec in bitvecs:
#     print(bitvec)