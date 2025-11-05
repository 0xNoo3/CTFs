from z3 import *
from constraints import Constraints, input

optimize = Optimize()

for i in range(64):
    optimize.add(input[i] >= 0x20)
    optimize.add(input[i] <= 0x7e)

for constraint in Constraints:
    optimize.add_soft(constraint)

flag = ""
if optimize.check() == sat:
    # print(optimize.model())
    model = optimize.model()
    # print(model)
    for index in input:
        flag += chr(model[index].as_long())
    print(flag)
