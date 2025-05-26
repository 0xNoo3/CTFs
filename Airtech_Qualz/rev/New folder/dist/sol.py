import string

# Define the character set: 0-9 and A-Z
CHARSET = string.digits + string.ascii_uppercase  # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to convert integer value to character
def int_to_char(i):
    if i < 10:
        return str(i)
    else:
        return chr(ord('A') + i - 10)

# Function to generate a key from starting values of four groups
def generate_key(start_values):
    key = ''
    for start in start_values:
        for i in range(4):
            val = start + i
            if val > 35:  # Ensure value stays within 0-35 (up to 'Z')
                return None
            key += int_to_char(val)
    return key

# Brute-force search for a valid key
def find_valid_key():
    # Starting values range from 0 to 32 (since 32 + 3 = 35, the max valid value)
    for s1 in range(0, 33):  # Group 1 starting value
        for s2 in range(s1 + 1, 33):  # Group 2 starting value, must be > s1
            for s3 in range(s2 + 1, 33):  # Group 3 starting value, must be > s2
                for s4 in range(s3 + 1, 33):  # Group 4 starting value, must be > s3
                    start_values = [s1, s2, s3, s4]
                    key = generate_key(start_values)
                    if key:
                        return key  # Return the first valid key found
    return None

# Main execution
if __name__ == "__main__":
    valid_key = find_valid_key()
    if valid_key:
        print(f"Found valid key: {valid_key}")
    else:
        print("No valid key found.")