import mpmath
import sympy

# The lookup table from the original code
TBL = [
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
    0x0000dc71, 0x000007f6, 0x00000208, 0x000016bc, 0x00000664, 0x00001f20, 0x0000077f, 0x00000ad4,
]

def luhn_check_9digits(num):
    """Luhn checksum algorithm for 9-digit numbers"""
    s = f"{num:09d}"
    lookup = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    total = 0
    toggle = True
    for digit_char in reversed(s):
        digit = int(digit_char)
        if toggle:
            total += digit
        else:
            total += lookup[digit]
        toggle = not toggle
    return (total % 10) == 0

# Set high precision and calculate pi
mpmath.mp.dps = 2000000
PI_STR = str(mpmath.mp.pi)[2:]  # Remove "3."

def get_pi_decimals(start_index):
    """Extract 9 digits from pi starting at given index"""
    return int(PI_STR[start_index-1:start_index-1+9], 10)

def check_character_at_position(char_byte, position, current_offset):
    """Check if a character satisfies all conditions at a given position"""
    # Calculate table index
    tbl_index = (current_offset + position * char_byte) & 0xFFFFFFFF
    tbl_index = tbl_index % 0xFF
    tbl_value = TBL[tbl_index]
    
    # Calculate new offset
    new_offset = (current_offset + tbl_value) & 0xFFFFFFFF
    
    # Get 9 digits from pi
    part = get_pi_decimals(new_offset)
    part_b1 = (part & 0xFF00) >> 8
    
    # Perform tests
    test0 = 0x20 <= char_byte <= 0x80  # Printable ASCII range
    test1 = part_b1 == char_byte       # Second byte matches character
    test2 = luhn_check_9digits(part)   # Luhn checksum passes
    test3 = sympy.isprime(part)        # Number is prime (commented out in original)
    
    return test0 and test1 and test2, new_offset, part

def find_valid_characters_at_position(position, current_offset):
    """Find all valid characters for a given position"""
    valid_chars = []
    
    # Test all printable ASCII characters
    for char_byte in range(0x20, 0x81):  # Space to DEL
        try:
            is_valid, new_offset, part_value = check_character_at_position(char_byte, position, current_offset)
            if is_valid:
                valid_chars.append((chr(char_byte), char_byte, new_offset, part_value))
        except (IndexError, ValueError):
            # Skip if we go out of bounds in pi digits
            continue
    
    return valid_chars

def solve_flag_recursive(target_sum, current_sum=0, current_flag="", position=0, offset=0, max_length=50):
    """Recursively find valid flags"""
    if current_sum == target_sum and position > 0:
        return [current_flag]
    
    if position >= max_length or current_sum > target_sum:
        return []
    
    results = []
    valid_chars = find_valid_characters_at_position(position, offset)
    
    for char, char_byte, new_offset, part_value in valid_chars:
        new_sum = current_sum + part_value
        if new_sum <= target_sum:  # Pruning: don't exceed target
            sub_results = solve_flag_recursive(
                target_sum, new_sum, current_flag + char, position + 1, new_offset, max_length
            )
            results.extend(sub_results)
    
    return results

def solve_flag():
    """Main solving function"""
    target_sum = 0x2c973df64
    print(f"Target sum: {target_sum}")
    print(f"Target sum (hex): 0x{target_sum:x}")
    
    print("Searching for valid flags...")
    
    # Try different maximum lengths
    for max_len in range(10, 31):  # Common flag lengths
        print(f"Trying maximum length: {max_len}")
        results = solve_flag_recursive(target_sum, max_length=max_len)
        
        if results:
            print(f"Found {len(results)} valid flag(s):")
            for flag in results:
                print(f"  {flag}")
            return results
        
        # Also try a more focused search for shorter flags
        if max_len <= 20:
            print(f"  No flags found with max length {max_len}")
    
    print("No valid flags found within reasonable length limits.")
    return []

def verify_flag(flag_str):
    """Verify a flag using the original algorithm"""
    flag = flag_str.encode()
    offset = 0
    sum_val = 0
    
    print(f"Verifying flag: {flag_str}")
    
    for i, c in enumerate(flag):
        tbl_index = (offset + i * c) & 0xFFFFFFFF
        tbl_index = tbl_index % 0xFF
        tbl_value = TBL[tbl_index]
        offset = (offset + tbl_value) & 0xFFFFFFFF
        part = get_pi_decimals(offset)
        part_b1 = (part & 0xFF00) >> 8
        
        test0 = 0x20 <= c <= 0x80
        test1 = part_b1 == c
        test2 = luhn_check_9digits(part)
        test3 = sympy.isprime(part)
        
        print(f"  Char {i}: '{chr(c)}' (0x{c:02x}) -> offset={offset}, part={part}")
        print(f"    Tests: ASCII={test0}, Match={test1}, Luhn={test2}, Prime={test3}")
        
        if not (test0 and test1 and test2):
            print(f"    FAILED at position {i}")
            return False
        
        sum_val += part
    
    result = sum_val == 0x2c973df64
    print(f"  Final sum: {sum_val} (0x{sum_val:x})")
    print(f"  Target:    {0x2c973df64} (0x{0x2c973df64:x})")
    print(f"  Valid: {result}")
    
    return result

if __name__ == "__main__":
    # Try to solve the flag
    flags = solve_flag()
    
    # If no flags found through exhaustive search, try some common patterns
    if not flags:
        print("\nTrying some common flag patterns...")
        test_flags = [
            "flag{test}",
            "CTF{test}",
            "flag{pi_challenge}",
            "flag{digits_of_pi}",
            "pi_flag",
            "flag{luhn_pi}",
        ]
        
        for test_flag in test_flags:
            if verify_flag(test_flag):
                print(f"Found valid flag: {test_flag}")
                break
    else:
        # Verify found flags
        for flag in flags:
            verify_flag(flag)