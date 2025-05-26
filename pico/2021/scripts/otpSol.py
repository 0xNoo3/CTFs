from z3 import *

# Given output string
output_str = "ztqittwtxtieyfrslgtzuxovlfdnbrsnlrvyhhsdxxrfoxnjbl"
length = len(output_str)

# Create a list of symbolic variables (the original password characters)
original_input = [Int(f"x_{i}") for i in range(length)]

solver = Solver()

# Constraints: Original characters should be lowercase letters ('a' to 'z')
for i in range(length):
    solver.add(original_input[i] >= ord('a'))
    solver.add(original_input[i] <= ord('z'))

# Function to apply the transformation (forward transformation from the C code)
def transform_char(c, i_1):
    uVar1 = (i_1 % 0xff >> 1 & 0x55) + (i_1 % 0xff & 0x55)
    uVar1 = ((uVar1 >> 2) & 0x33) + (uVar1 & 0x33)
    iVar2 = ((uVar1 >> 4) + c - 0x61 + (uVar1 & 0xf))
    return (iVar2 % 26) + ord('a')

# Apply the reverse process: We start with `original_input`, apply the transformation three times, and get `output_str`
transformed = original_input[:]  # Start with original input
for _ in range(3):  # Apply transformation 3 times
    transformed = [transform_char(transformed[i], i) for i in range(length)]

# Constrain Z3 solver to ensure that transformed input equals the output string
for i in range(length):
    solver.add(transformed[i] == ord(output_str[i]))

# Solve the equations
if solver.check() == sat:
    model = solver.model()
    flag = "".join(chr(model[original_input[i]].as_long()) for i in range(length))
    print("Recovered Password:", flag)
else:
    print("No solution found")
