def create_mapping():
    # Example mapping based on the hint
    return {
        'u': '49',
        't': '34',
        'f': '48',
        'l': '39',
        'a': '36',
        'g': '37'
    }

def decrypt(encrypted_string, mapping):
    decrypted = ""
    i = 0
    while i < len(encrypted_string):
        matched = False
        for char, num in mapping.items():
            if encrypted_string.startswith(num, i):
                decrypted += char
                i += len(num)
                matched = True
                break
        if not matched:
            decrypted += '?'  # Indicate an unmatched segment
            i += 1  # Move to the next character
    return decrypted

# Example usage
mapping = create_mapping()
encrypted_string = "4934849349493674935749360493664926549265492654926549265492654926549265492654926549265492654926549265492654926549265492654926549265492654926549265492654926549265492654926549265"
decrypted_flag = decrypt(encrypted_string, mapping)
print(decrypted_flag)