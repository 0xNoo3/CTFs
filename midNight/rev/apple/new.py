#!/usr/bin/env python3
import math
from decimal import Decimal, getcontext

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def luhn_checksum(n):
    """Luhn algorithm checksum validation"""
    # Convert to 9-digit string with leading zeros
    s = f"{n:09d}"
    
    # Luhn doubling table for efficiency
    double_table = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    
    total = 0
    alternate = True
    
    # Process from right to left
    for i in range(len(s) - 1, -1, -1):
        digit = int(s[i])
        if not alternate:
            digit = double_table[digit]
        total += digit
        alternate = not alternate
    
    return total % 10 == 0

def simplified_spigot(input_val):
    """
    Simplified version of the spigot function
    The original is very complex, so we'll approximate it
    """
    # The spigot function seems to be computing something related to pi
    # but the exact implementation is complex. For now, we'll return the input
    # as a starting approximation and refine based on testing
    return input_val

def modular_exponentiation(base, exponent, modulus):
    """Fast modular exponentiation"""
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def generate_lookup_table():
    """The actual lookup table from DAT_100008000"""
    table = [
        0x0000b4da, 0x0000083b, 0x0000139d, 0x0000084e, 0x00001251, 0x000008fa, 0x00001a55, 0x00000346,
        0x00000d3d, 0x00001496, 0x0000100e, 0x00001ef9, 0x00001cb7, 0x00018ebb, 0x000004a8, 0x00001269,
        0x000007c3, 0x00001219, 0x00001ea4, 0x000001ea, 0x00009318, 0x0000a994, 0x0000805a, 0x00000daf,
        0x000014c1, 0x00000180, 0x00001bd2, 0x000001a0, 0x0000127a, 0x00000403, 0x00001fee, 0x00001790,
        0x00000baf, 0x00000900, 0x00001203, 0x00001519, 0x000015a5, 0x0000078e, 0x00001375, 0x0000141d,
        0x00000b67, 0x000008fb, 0x00001b69, 0x0000c88d, 0x000012a5, 0x00001057, 0x00001c42, 0x0000086d,
        0x000127b9, 0x00001620, 0x0000013e, 0x0000013e, 0x000003a2, 0x0000021b, 0x00001498, 0x00000c1f,
        0x00001e6f, 0x00000b42, 0x00001cd9, 0x00001971, 0x000010d8, 0x00000839, 0x00002c8d, 0x000003ac,
        0x00001a05, 0x00000e3d, 0x000014be, 0x00000fb5, 0x00001b3e, 0x0000106f, 0x00001675, 0x00001ed3,
        0x00001f89, 0x0000103f, 0x00000f22, 0x00001294, 0x0000512b, 0x00001cf8, 0x000011ed, 0x00000d95,
        0x00001417, 0x00001e5c, 0x00000a93, 0x00000186, 0x00000809, 0x00001524, 0x00001d68, 0x0000e729,
        0x00000eb5, 0x00000671, 0x0000185c, 0x00001fc8, 0x0000193f, 0x0000019c, 0x00001c8c, 0x000009fb,
        0x00001ea6, 0x00001023, 0x00001b4f, 0x00001697, 0x000008d6, 0x00000a99, 0x0000114b, 0x00002908,
        0x000018f3, 0x00012ceb, 0x000008a6, 0x00001c86, 0x00001ab9, 0x00000291, 0x0000109e, 0x000018b4,
        0x00000b27, 0x00001042, 0x00001d02, 0x00001a4e, 0x0000070f, 0x00001776, 0x00001712, 0x00001dce,
        0x00001397, 0x00000a00, 0x00000742, 0x00001d57, 0x00000f0f, 0x00000ffe, 0x000007fa, 0x00001e02,
        0x00000848, 0x00000509, 0x0000156d, 0x00000858, 0x00000dc5, 0x0000048c, 0x0000019d, 0x0000034f,
        0x0000063e, 0x00000c7f, 0x00001de2, 0x00000b5b, 0x00000585, 0x000018bb, 0x00000a93, 0x00000975,
        0x000015d5, 0x0000023a, 0x000006fd, 0x000007fd, 0x00000d27, 0x00000f01, 0x000018a0, 0x00000d62,
        0x000017ea, 0x00000fbe, 0x0000053e, 0x00000308, 0x00000701, 0x00000e65, 0x00001b0c, 0x00001262,
        0x000013c7, 0x00000634, 0x0000121b, 0x00000918, 0x00001bdb, 0x0000055f, 0x0000c5d2, 0x000013aa,
        0x0000152f, 0x00001e4a, 0x00000b0f, 0x00000500, 0x00000139, 0x00000820, 0x000011de, 0x0000014d,
        0x00007986, 0x00001d59, 0x00001dcc, 0x00001434, 0x0000187b, 0x0000160a, 0x00000153, 0x00010ee4,
        0x00000901, 0x00000a5c, 0x00001695, 0x00001653, 0x000012c2, 0x00001ba6, 0x00001788, 0x000049aa,
        0x00000506, 0x00020de1, 0x000017ee, 0x0000178d, 0x00000d68, 0x000010ed, 0x000010fd, 0x00000cd0,
        0x000006a3, 0x000010c2, 0x0000122f, 0x00001bb8, 0x000002d7, 0x00001a1a, 0x00000ae6, 0x00001ebe,
        0x00001d3e, 0x000009c7, 0x00001827, 0x00000690, 0x00001738, 0x000004fa, 0x0000120a, 0x0000127d,
        0x00000e96, 0x00001f22, 0x0000059e, 0x00001c7e, 0x00001cc8, 0x000009b4, 0x00001bf8, 0x00001ff1,
        0x000012a3, 0x00000a76, 0x00001572, 0x000006ca, 0x00000d69, 0x000003b7, 0x00000280, 0x00001c0f,
        0x00000a53, 0x0000134f, 0x00000726, 0x00000a8c, 0x00001388, 0x00002651, 0x00000bd7, 0x00001df2,
        0x000013fe, 0x00001d87, 0x00000b31, 0x0000058e, 0x00001280, 0x00009519, 0x00001434, 0x00000ae6,
        0x0000dc71, 0x000007f6, 0x00000208, 0x000016bc, 0x00000664, 0x00001f20, 0x0000077f, 0x00000ad4
    ]
    return table

def solve_challenge():
    """Main solver function with systematic approach"""
    target_sum = 0x2c973df64  # 12079259492
    lookup_table = generate_lookup_table()
    
    print(f"Target sum: {target_sum}")
    print("Searching for valid input string...")
    
    # Try different string lengths systematically
    for length in range(1, 30):  # Extended range
        print(f"Trying length {length}...")
        
        # Try different approaches for each length
        found = False
        
        # Approach 1: Common flag patterns
        if try_flag_patterns(length, target_sum, lookup_table):
            found = True
        
        # Approach 2: Brute force with smart pruning
        if not found and length <= 8:  # Only brute force short strings
            if brute_force_search(length, target_sum, lookup_table):
                found = True
        
        # Approach 3: Mathematical approach - work backwards from target
        if not found:
            if mathematical_approach(length, target_sum, lookup_table):
                found = True
        
        if found:
            break
    
    print("Search completed.")

def try_flag_patterns(length, target_sum, lookup_table):
    """Try common CTF flag patterns"""
    patterns = []
    
    # Standard flag formats
    if length >= 5:
        patterns.append("flag{" + "A" * (length - 6) + "}")
    if length >= 4:
        patterns.append("CTF{" + "A" * (length - 5) + "}")
        patterns.append("FLAG" + "A" * (length - 4))
    
    # Try with different fill characters
    fill_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    for pattern_base in ["flag{", "FLAG{", "CTF{", "ctf{"]:
        if length <= len(pattern_base) + 1:
            continue
        
        inner_length = length - len(pattern_base) - 1  # -1 for closing brace
        
        # Try single character fills
        for char in fill_chars:
            test_string = pattern_base + char * inner_length + "}"
            if validate_string_debug(test_string, target_sum, lookup_table):
                print(f"Found valid string: {test_string}")
                return True
    
    return False

def brute_force_search(length, target_sum, lookup_table):
    """Brute force search for short strings"""
    import itertools
    
    # Printable ASCII range that passes initial check (0x1f < char < 0x80)
    valid_chars = [chr(i) for i in range(0x20, 0x7f)]  # Space to DEL-1
    
    print(f"Brute forcing length {length} with {len(valid_chars)} characters...")
    
    count = 0
    for combo in itertools.product(valid_chars, repeat=length):
        test_string = ''.join(combo)
        count += 1
        
        if count % 100000 == 0:
            print(f"Tested {count} combinations...")
        
        if validate_string_debug(test_string, target_sum, lookup_table):
            print(f"Found valid string: {test_string}")
            return True
    
    return False

def mathematical_approach(length, target_sum, lookup_table):
    """Try to work backwards from the target sum"""
    # This is a heuristic approach
    # We know the sum needs to equal target_sum
    # Average contribution per character would be target_sum / length
    
    avg_contribution = target_sum // length
    print(f"Average contribution per character should be: {avg_contribution}")
    
    # Look for characters that might produce values near this average
    # This is still complex due to the spigot function, but we can try
    
    return False

def validate_string_debug(s, target_sum, lookup_table):
    """Enhanced validation with debug output for the first few attempts"""
    local_24 = 0  # Accumulator from the original code
    local_30 = 0  # Sum of valid values
    debug_info = []
    
    for i, char in enumerate(s):
        char_val = ord(char)
        
        # Check if character is in valid range (0x1f < char < 0x80)
        if not (0x1f < char_val < 0x80):
            return False
        
        # Calculate lookup table index (same as original algorithm)
        index = (i * char_val + local_24) % 0xff
        table_value = lookup_table[index]
        local_24 += table_value
        
        # Get spigot value - using simplified version for now
        spigot_val = simplified_spigot(local_24)
        
        # Check if character matches spigot high byte
        expected_char = (spigot_val & 0xff00) >> 8
        if char_val != expected_char:
            continue
        
        # Check if spigot_val passes prime test
        if not is_prime(spigot_val):
            continue
        
        # Check if spigot_val passes Luhn checksum
        if not luhn_checksum(spigot_val):
            continue
        
        # If all tests pass, add to sum
        local_30 += spigot_val
        debug_info.append(f"Char '{char}' ({char_val}) -> spigot: {spigot_val}, sum: {local_30}")
    
    # Debug output for promising attempts
    if local_30 > target_sum * 0.1:  # If we're getting somewhere
        print(f"String '{s}' achieved sum: {local_30} (target: {target_sum})")
        if len(debug_info) <= 10:  # Don't spam too much
            for info in debug_info:
                print(f"  {info}")
    
    return local_30 == target_sum

def find_string_of_length(length, target_sum, lookup_table):
    """Find a valid string of specified length"""
    
    # For a brute force approach, we'd need to try all combinations
    # This is computationally intensive, so we'll use a heuristic approach
    
    # Try common patterns first
    test_strings = [
        "flag{" + "A" * (length - 6) + "}" if length > 6 else "A" * length,
        "CTF{" + "A" * (length - 5) + "}" if length > 5 else "A" * length,
        "FLAG" + "A" * (length - 4) if length > 4 else "A" * length,
        "test" + "A" * (length - 4) if length > 4 else "test"[:length],
        "password"[:length],
        "secret"[:length],
        "key"[:length],
    ]
    
    for test_string in test_strings:
        if len(test_string) != length:
            continue
            
        if validate_string(test_string, target_sum, lookup_table):
            print(f"Found valid string: {test_string}")
            return True
    
    return False

def validate_string(s, target_sum, lookup_table):
    """Validate if a string satisfies all conditions - simplified for testing"""
    local_24 = 0  # Accumulator from the original code
    local_30 = 0  # Sum of valid values
    
    for i, char in enumerate(s):
        char_val = ord(char)
        
        # Check if character is in valid range (0x1f < char < 0x80)
        if not (0x1f < char_val < 0x80):
            return False
        
        # Calculate lookup table index
        index = (i * char_val + local_24) % 0xff
        local_24 += lookup_table[index]
        
        # Get spigot value (simplified for now)
        spigot_val = simplified_spigot(local_24)
        
        # Check if character matches spigot high byte
        if char_val != ((spigot_val & 0xff00) >> 8):
            continue
        
        # Check if spigot_val passes prime test
        if not is_prime(spigot_val):
            continue
        
        # Check if spigot_val passes Luhn checksum
        if not luhn_checksum(spigot_val):
            continue
        
        # If all tests pass, add to sum
        local_30 += spigot_val
    
    return local_30 == target_sum

def extract_flag_format():
    """Try to extract flag in common CTF formats"""
    print("Attempting to find flag format...")
    
    # Common CTF flag prefixes
    prefixes = ["flag{", "FLAG{", "CTF{", "ctf{"]
    
    for prefix in prefixes:
        print(f"Trying prefix: {prefix}")
        # Would implement more sophisticated search here
        
    print("Manual analysis may be required to extract the exact lookup table")
    print("and implement the precise spigot algorithm from the binary.")

def analyze_spigot_behavior():
    """Analyze the spigot function behavior to understand the pattern"""
    print("Analyzing spigot function behavior...")
    
    # Test the spigot function with various inputs to understand its behavior
    test_inputs = [100, 500, 1000, 5000, 10000, 50000, 100000]
    
    for inp in test_inputs:
        result = simplified_spigot(inp)
        high_byte = (result & 0xff00) >> 8
        
        print(f"Input: {inp:6d} -> Spigot: {result:8d} -> High byte: {high_byte:3d} ('{chr(high_byte) if 32 <= high_byte <= 126 else '?'}')")
        
        # Check if this could be part of a flag
        if 32 <= high_byte <= 126:
            char = chr(high_byte)
            if char.isalnum() or char in "{}[]()_-":
                print(f"  -> Potential flag character: '{char}'")

def test_known_patterns():
    """Test with some known patterns to see if we can reverse engineer the spigot function"""
    lookup_table = generate_lookup_table()
    
    # Test common flag starts
    test_strings = ["flag{", "FLAG{", "CTF{", "test", "hello"]
    
    for test_str in test_strings:
        print(f"\nTesting '{test_str}':")
        local_24 = 0
        
        for i, char in enumerate(test_str):
            char_val = ord(char)
            index = (i * char_val + local_24) % 0xff
            table_value = lookup_table[index]
            local_24 += table_value
            
            spigot_result = simplified_spigot(local_24)
            high_byte = (spigot_result & 0xff00) >> 8
            
            print(f"  Char '{char}' -> local_24: {local_24} -> spigot: {spigot_result} -> high_byte: {high_byte}")
            
            # Check what character this high byte represents
            if 32 <= high_byte <= 126:
                expected_char = chr(high_byte)
                match = "✓" if expected_char == char else "✗"
                print(f"    Expected char: '{expected_char}' {match}")

if __name__ == "__main__":
    print("Reverse Engineering Challenge Solver")
    print("=" * 50)
    
    # First, let's understand the spigot function better
    analyze_spigot_behavior()
    print("\n" + "="*50)
    
    # Test some patterns to understand the algorithm
    test_known_patterns()
    print("\n" + "="*50)
    
    # Run the main solver
    solve_challenge()