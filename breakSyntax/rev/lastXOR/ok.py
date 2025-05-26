#!/usr/bin/env python3

import subprocess

for key in range(256):
    try:
        result = subprocess.run(
            ["./lastXOR", f"{key}"],
            capture_output=True,
            text=True,
            timeout=1
        )

        output = result.stdout + result.stderr

        print(f"[+] Tried key: {key} — Output: {output.strip()}")

        if "BtSCTF{" in output:
            print(f"\n[+] Found key: {key} (0x{key:02x})")
            print(f"Flag: {output.strip()}")
            break

    except subprocess.TimeoutExpired:
        print(f"[-] Timeout on key {key}, skipping.")
    except Exception as e:
        print(f"[-] Error on key {key}: {e}")
