import re

code = """
v33 = input[11];
v32 = input[18];
if ( (input[7] - v33 + v32) >= 0x52u )
"""


# Step 1: extract mappings
mapping = dict(re.findall(r'(v\d+)\s*=\s*(input\[\d+\]);', code))

# Step 2: replace in code
for var, repl in mapping.items():
    code = re.sub(rf'\b{var}\b', repl, code)

print(f" After Replacement : {code}")
code = re.sub(rf'input\[\d+\]\s*.\s*input\[\d+\];', '', code)
print(f" After Deletion : {code}")

code = re.sub(rf'0x([0-9A-Fa-f]+)u', r'0x\1', code)

print(f'Final code : {code}')


