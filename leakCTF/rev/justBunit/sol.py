def round3(x):
    return round(x * 1000.0) / 1000.0

# Emulate sub_404605: Conditional transformation logic
def transform(x):
    if x < 0.0 or x >= 1.0:
        return round3(x)
    elif x < 0.25:
        x += 0.55
    elif x < 0.55:
        x -= 0.25
    elif x < 0.75:
        x += 0.2
    else:
        x -= 0.5
    return round3(x)

# Optimized version of sub_40473D with cycle detection
def apply_n_times_fast(n, x):
    seen = {}
    i = 0
    while i < n:
        if x in seen:
            # Detected a cycle
            cycle_start = seen[x]
            cycle_len = i - cycle_start
            remaining = (n - i) % cycle_len
            for _ in range(remaining):
                x = transform(x)
            return x
        seen[x] = i
        x = transform(x)
        i += 1
    return x

# Use the correct charset found at address 0x5e57b0
def get_charset():
    return "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{_}"

# Combine all logic
def simulate(n, x, charset):
    y = apply_n_times_fast(n, x)
    index = int(y * 100.0) % len(charset)
    return charset[index]

# Load input pairs from the original file or array (example shown here)
import json

with open("input.txt") as f:
    input_data = json.load(f)

# Run simulation
charset = get_charset()
flag = ''.join(simulate(n, x, charset) for n, x in input_data)

print("Final Flag:", flag)