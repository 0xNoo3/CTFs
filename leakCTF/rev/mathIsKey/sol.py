#!/usr/bin/env python3
import subprocess, re, struct, sys

BIN = "./final"

def extract_keys():
    # We’ll run the binary under GDB’s Python API to grab each checked value
    # without you having to do anything by hand.
    gdb_script = r'''
set pagination off
file {bin}
# breakpoint right after each scanf, before the cmp
break *0x40310f
break *0x4032xx  # second scanf address – you’ll need to fill these in
break *0x4034xx  # third scanf
break *0x4036xx  # fourth scanf
break *0x4038xx  # fifth scanf
run
# On each hit, print the just‐read unsigned long (in rax)
commands
  silent
  printf "%llu\n", $rax
  continue
end
'''.format(bin=BIN)

    # Write temporary gdb script
    with open("gdb.script", "w") as f:
        f.write(gdb_script)

    # Run GDB in batch mode
    out = subprocess.check_output(["gdb", "-q", "-x", "gdb.script"]).decode()
    # Extract the five numbers
    nums = re.findall(r'(\d+)\n', out)
    if len(nums) != 5:
        print("Error: expected 5 keys, got", nums, file=sys.stderr)
        sys.exit(1)
    return nums

def decode_flag(nums):
    # Build the single large decimal string:
    a_str = "".join(nums) + "804300"
    a = int(a_str)
    # Convert to 32‐byte little endian
    b = a.to_bytes(32, 'little')
    # Strip trailing NULs and decode
    return b.rstrip(b'\x00').decode('ascii')

if __name__ == "__main__":
    keys = extract_keys()
    print("Recovered key values:")
    for i,k in enumerate(keys,1):
        print(f"  Key {i}: {k}")
    flag = decode_flag(keys)
    print("\n*** FLAG: ", flag)
