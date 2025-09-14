#!/usr/bin/env python3
"""
Static analysis solution for the reverse engineering challenge.
This extracts and reverses the core transformation algorithm.
"""

def hash_string_ignore_case(s):
    """Replicate the hash function from the binary"""
    result = 0
    for c in s:
        i = ord(c)
        if 97 <= i <= 122:  # lowercase a-z
            i -= 32  # convert to uppercase
        # ROR4(result, 13) = ((result >> 13) | (result << (32-13))) & 0xFFFFFFFF
        result = ((result >> 13) | (result << 19)) & 0xFFFFFFFF
        result = (i + result) & 0xFFFFFFFF
    return result

def xorshift_prng(seed):
    """
    Replicate the PRNG used in the binary.
    Based on the assembly at 0x7FF683DF1200 and 0x7FF683DF158A
    """
    x = seed & 0xFFFFFFFF
    while True:
        # x ^= x << 13
        x ^= (x << 13) & 0xFFFFFFFF
        # x ^= x >> 17  
        x ^= x >> 17
        # x ^= x << 5
        x ^= (x << 5) & 0xFFFFFFFF
        x &= 0xFFFFFFFF
        yield x

def calculate_seed():
    """Calculate the PRNG seed from API name hashes"""
    h1 = hash_string_ignore_case("LoadLibraryA")
    h2 = hash_string_ignore_case("GetProcAddress") 
    h3 = hash_string_ignore_case("VirtualProtect")
    h4 = hash_string_ignore_case("IsDebuggerPresent")
    
    # From assembly: imul by 0x21, 0x61, 0x83, 0x7 respectively
    seed = (0x21 * h1) ^ (0x61 * h2) ^ (0x83 * h3) ^ (0x7 * h4)
    seed &= 0xFFFFFFFF
    
    print(f"Calculated hashes:")
    print(f"  LoadLibraryA: 0x{h1:08x}")
    print(f"  GetProcAddress: 0x{h2:08x}") 
    print(f"  VirtualProtect: 0x{h3:08x}")
    print(f"  IsDebuggerPresent: 0x{h4:08x}")
    print(f"PRNG Seed: 0x{seed:08x}")
    
    return seed

def generate_operations(seed, num_ops=64):
    """
    Generate the sequence of XOR operations based on the PRNG.
    This replicates the loop at 0x7FF683DF158A in the assembly.
    """
    prng = xorshift_prng(seed)
    operations = []
    
    for _ in range(num_ops):
        # Get next random value
        rand1 = next(prng)
        
        # Calculate operation parameters (from assembly logic)
        # rand1 % 5 + 1 gives operation length (1-5)
        op_len = (rand1 % 5) + 1
        
        # Calculate range: 36 - op_len  
        range_size = 36 - op_len
        
        # Get two more random values
        rand2 = next(prng) 
        rand3 = next(prng)
        
        # Calculate positions
        pos1 = rand2 % range_size
        pos2 = rand3 % range_size
        
        # If positions are same, adjust second one
        if pos1 == pos2:
            pos2 = (pos2 + 7) % range_size
            
        operations.append((pos1, pos2, op_len))
        
    return operations

def apply_operations(data, operations):
    """Apply the XOR operations to transform the data"""
    result = bytearray(data)
    
    for pos1, pos2, length in operations:
        # XOR data[pos1:pos1+length] with data[pos2:pos2+length]
        for i in range(length):
            if pos1 + i < len(result):
                if pos2 + i < len(result):
                    result[pos1 + i] ^= result[pos2 + i - pos1 + pos2]
                    
    return bytes(result)

def reverse_operations(data, operations):
    """Reverse the XOR operations (XOR is its own inverse)"""
    # Apply operations in reverse order
    result = bytearray(data)
    
    for pos1, pos2, length in reversed(operations):
        for i in range(length):
            if pos1 + i < len(result):
                if pos2 + i < len(result):
                    result[pos1 + i] ^= result[pos2 + i - pos1 + pos2]
                    
    return bytes(result)

def extract_target_from_binary(binary_path):
    """
    Extract the 35-byte target from unk_7FF683DF40E0.
    You need to provide the binary file and the correct offset.
    """
    try:
        with open(binary_path, 'rb') as f:
            # You need to find the correct file offset for 0x7FF683DF40E0
            # This is typically: RVA - ImageBase + FileOffset 
            # For now, return placeholder - you need to extract this manually
            target_offset = 0x1234  # REPLACE WITH ACTUAL OFFSET
            f.seek(target_offset)
            target = f.read(35)
            return target
    except:
        # Placeholder target - replace with actual extracted bytes
        print("Warning: Using placeholder target. Extract real target from binary!")
        return b"PLACEHOLDER_TARGET_35_BYTES_HERE!!"

def solve_challenge(binary_path=None):
    """Main solving function"""
    print("=== Reverse Engineering Challenge Solver ===\n")
    
    # Step 1: Calculate PRNG seed
    seed = calculate_seed()
    
    # Step 2: Generate operation sequence  
    print(f"\nGenerating operation sequence...")
    operations = generate_operations(seed)
    
    print(f"Generated {len(operations)} operations:")
    for i, (p1, p2, length) in enumerate(operations[:5]):
        print(f"  Op {i}: XOR pos {p1} with pos {p2}, length {length}")
    print("  ...")
    
    # Step 3: Extract target
    target = None
    if binary_path:
        target = extract_target_from_binary(binary_path)
        if target and len(target) == 35:
            print(f"\nExtracted target: {target.hex()}")
            
            # Check if it looks like code (bad extraction)
            if target.startswith(b'\x8b\x40') or target.startswith(b'\x48\x8b'):
                print("WARNING: Target looks like x86 code, not data!")
                print("This suggests wrong file offset. You need to manually find unk_7FF683DF40E0")
                target = None
    
    if not target:
        print("\nCannot automatically extract target from binary.")
        print("You need to manually find the 35 bytes at unk_7FF683DF40E0")
        print("\nOptions:")
        print("1. Use a disassembler (IDA Pro/Ghidra) to find unk_7FF683DF40E0")
        print("2. Set breakpoint after 'rep movsb' and dump memory")
        print("3. Search for the data section containing this address")
        
        # Let's still show what the algorithm would do with a test input
        print("\nFor testing, let's see what operations would be applied:")
        test_input = b"A" * 35  # Test with all A's
        print(f"Test input: {test_input}")
        
        transformed = apply_operations(test_input, operations)
        print(f"Would transform to: {transformed.hex()}")
        
        return None
    
    # Step 4: Reverse the operations to find the original input
    print(f"\nReversing operations...")
    try:
        original = reverse_operations(target, operations)
        print(f"Reversed result: {original}")
        
        # Step 5: Verify by applying forward transformation
        print("\nVerification:")
        transformed = apply_operations(original, operations)
        print(f"Forward transform: {transformed.hex()}")
        print(f"Target:           {target.hex()}")
        print(f"Matches target: {transformed == target}")
        
        if transformed == target:
            try:
                flag = original.decode('ascii', errors='replace')
                print(f"\n*** POTENTIAL FLAG: {flag} ***")
            except:
                print(f"\nFlag (bytes): {original}")
                print(f"Flag (hex): {original.hex()}")
        else:
            print("Verification failed - algorithm may be incorrect")
            
        return original
        
    except Exception as e:
        print(f"Error during operation reversal: {e}")
        print("This suggests the algorithm implementation needs refinement")
        return None

def manual_target_input():
    """Helper to manually input the target if you have it"""
    print("Enter the 35-byte target as hex (without spaces):")
    hex_input = input("> ").strip()
    
    try:
        target = bytes.fromhex(hex_input)
        if len(target) != 35:
            print(f"Error: Expected 35 bytes, got {len(target)}")
            return None
        return target
    except ValueError:
        print("Error: Invalid hex input")
        return None

if __name__ == "__main__":
    import sys
    
    print("Choose option:")
    print("1. Solve with binary file")
    print("2. Solve with manual target input") 
    print("3. Just show algorithm analysis")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        if len(sys.argv) > 1:
            solve_challenge(sys.argv[1])
        else:
            binary_path = input("Enter binary file path: ").strip()
            solve_challenge(binary_path)
            
    elif choice == "2":
        target = manual_target_input()
        if target:
            seed = calculate_seed()
            operations = generate_operations(seed)
            original = reverse_operations(target, operations)
            
            # Verify
            transformed = apply_operations(original, operations)
            if transformed == target:
                try:
                    flag = original.decode('ascii')
                    print(f"\n*** FLAG: {flag} ***")
                except:
                    print(f"\nFlag (bytes): {original}")
            else:
                print("Verification failed - check the algorithm")
                
    else:
        # Just show the analysis
        seed = calculate_seed()
        operations = generate_operations(seed, 10)  # Just show first 10
        print("\nFirst 10 operations would be:")
        for i, (p1, p2, length) in enumerate(operations):
            print(f"  Op {i}: XOR data[{p1}:{p1+length}] with data[{p2}:{p2+length}]")