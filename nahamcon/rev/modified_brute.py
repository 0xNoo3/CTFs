#!/usr/bin/env python3
import subprocess
import os
from multiprocessing import Process, Event, Queue

CANDIDATES_FILE = "candidates.txt"
BIN_PATH        = "./flagsflags"
BAD_MARKER      = "Incorrect flag!"
START_OFFSETS   = [900, 1900, 2900, 3900]

def worker(worker_id, flags, offset, total, stop_evt, out_q):
    """
    Each worker starts from its given offset and tests flags sequentially.
    """
    for i, flag in enumerate(flags[offset:], start=offset):
        if stop_evt.is_set():
            return

        print(f"[W{worker_id}] Testing [{i}/{total}]: {flag}", flush=True)

        proc = subprocess.run(
            [BIN_PATH],
            input=flag + "\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        output = proc.stdout
        if BAD_MARKER not in output:
            out_q.put((flag, output.strip()))
            stop_evt.set()
            return

def main():
    # Load all flags
    with open(CANDIDATES_FILE) as f:
        flags = [line.strip() for line in f if line.strip()]
    total = len(flags)
    print(f"[*] Loaded {total} candidates.\n")

    # Setup multiprocessing
    stop_evt = Event()
    out_q    = Queue()
    procs    = []

    # Spawn exactly 4 workers at custom offsets
    for worker_id, offset in enumerate(START_OFFSETS):
        if offset >= total:
            continue
        p = Process(target=worker, args=(worker_id, flags, offset, total, stop_evt, out_q))
        p.start()
        procs.append(p)

    # Wait for one to succeed
    flag, output = out_q.get()
    print(f"\n✅ Found candidate: {flag}")
    print("--- Program output:")
    print(output)

    # Terminate others
    stop_evt.set()
    for p in procs:
        p.join()

if __name__ == "__main__":
    main()
