#!/usr/bin/env python3
# angr_find_input.py
# Usage: python3 angr_find_input.py <binary>
#
# This script uses the offsets you gave:
#   bcmp call (compare): .text:0x9D22
#   failed branch label: .text:0xA186
#   success print      : .text:0xA256
#
# The script computes mapped_base + these offsets so it works for PIE or non-PIE binaries.

import angr, claripy, sys, logging, os

logging.getLogger('angr').setLevel(logging.ERROR)

if len(sys.argv) != 2:
    print("Usage: python3 angr_find_input.py <binary>")
    sys.exit(1)

BINARY = sys.argv[1]

# offsets from your disassembly (text-relative)
OFF_BCMP = 0x9D22
OFF_FAIL = 0xA186
OFF_SUCCESS = 0xA256

# symbolic stdin length (bytes) — the program expects a single grapheme, but 8 bytes is safe to start
SYMBOLIC_STDIN_BYTES = 8

# Create project
proj = angr.Project(BINARY, auto_load_libs=False)

# compute runtime addresses (handles PIE)
base = proj.loader.main_object.mapped_base
addr_bcmp = base + OFF_BCMP
addr_fail = base + OFF_FAIL
addr_success = base + OFF_SUCCESS

print("[*] Binary:", BINARY)
print(f"[*] mapped_base = 0x{base:x}")
print(f"[*] bcmp (call) target address   = 0x{addr_bcmp:x}  (rel .text:0x{OFF_BCMP:x})")
print(f"[*] failure branch (avoid)       = 0x{addr_fail:x}  (rel .text:0x{OFF_FAIL:x})")
print(f"[*] success print (find)         = 0x{addr_success:x}  (rel .text:0x{OFF_SUCCESS:x})")

# Create symbolic stdin
sym_stdin = claripy.BVS('stdin', SYMBOLIC_STDIN_BYTES*8)

state = proj.factory.full_init_state(
    args=[BINARY],
    stdin=angr.SimFileStream(name='stdin', content=sym_stdin, size=SYMBOLIC_STDIN_BYTES),
    add_options={angr.options.LAZY_SOLVES}
)

# Optionally constrain newline if program expects newline-terminated input:
# state.solver.add(sym_stdin.get_byte(SYMBOLIC_STDIN_BYTES-1) == ord('\n'))

simgr = proj.factory.simulation_manager(state)

print("[*] Starting exploration (find success / avoid fail). This may take some time but usually is quick.")
# explore: find success, avoid fail
simgr.explore(find=addr_success, avoid=addr_fail, n=1)

if simgr.found:
    found = simgr.found[0]
    # Extract stdin bytes from the solved symbolic variable if possible
    try:
        concrete = found.solver.eval(sym_stdin, cast_to=bytes)
        # strip trailing zeros (if any)
        concrete = concrete.rstrip(b'\x00')
        print("\n[+] Found a concrete stdin that reaches the success print!")
        print("    stdin (hex):", concrete.hex())
        try:
            print("    stdin (utf-8):", concrete.decode('utf-8', errors='replace'))
        except:
            pass
        # also show the posix stdin dump (complete file)
        print("    full stdin dump (posix):", found.posix.dumps(0))
    except Exception as e:
        print("[!] Found state but failed to concretize sym_stdin:", e)
        # fallback: print posix stdin
        print("    posix stdin dump:", found.posix.dumps(0))
else:
    print("[-] No state reached the success address.")
    # show some information about stashes
    print("    active paths:", len(simgr.active))
    print("    deadended:", len(simgr.deadended))
    print("    errored:", len(simgr.errored))
    # optional: try exploring without avoid to see where paths end up
    # simgr.explore(find=addr_success, n=1)

