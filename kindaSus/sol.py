import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

FLAG = "JlLScp2qTzfFZ7kIYP6Jm5Mv/2h6p26S0OWgmXYdEMAl1Sjg6hwW95bPsZdtiggvHVVv8zM+x7vRw2qOr3ORbw=="
key = "ChKeFe"  # Derived from our valid path: Cemetery of Ash -> Firelink Shrine -> Kiln of the First Flame

# Derive the AES key from the key string.
privateKey = hashlib.sha256(key.encode("utf-8")).digest()

# Base64-decode the encrypted FLAG.
encryptedData = base64.b64decode(FLAG)
iv = encryptedData[:16]
ciphertext = encryptedData[16:]

# Set up AES decryption in CBC mode.
cipher = AES.new(privateKey, AES.MODE_CBC, iv)
decryptedBytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
decrypted_text = decryptedBytes.decode()

print("Decrypted flag:", decrypted_text)
