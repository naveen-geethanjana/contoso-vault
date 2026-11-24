# Number of letters in the English alphabet
ALPHABET_SIZE = 26

# Get the message and encyption key
message: str = input("Message: ")
key: int = int(input("Key: "))

# Empty string to store the encrypted message
ciphertext: str = ""

# Encrytion process
for letter in message:

    # Shift uppercase letters within the alphabet
    if "A" <= letter<= 'Z':
        shifted: int = ord(letter) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)

    # Shift lowercase letters within the alphabet
    elif "a" <= letter<= 'z':
        shifted: int = ord(letter) + key
        if shifted > ord("z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)

    # Preserve numbers, spaces, and special characters
    else:
        ciphertext += letter

# Display the encrypted message
print("Ciphertext:", ciphertext)

# Empty string to store the decrypted ciphertext
plaintext: str = ""

# Decrytion process
for letter in ciphertext:

    # Reverse the shift for uppercase letters within the alphabet
    if "A" <= letter<= 'Z':
        shifted: int = ord(letter) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)

    # Reverse the shift for lowercase letters within the alphabet
    elif "a" <= letter<= 'z':
        shifted: int = ord(letter) - key
        if shifted < ord("a"):
            shifted += ALPHABET_SIZE
        ciphertext += chr(shifted)

    # Preserve numbers, spaces, and special characters   
    else:
        plaintext += letter

# Display the decrypted ciphertext
print("Plaintext:", plaintext)

# Verify decryption restores the original message
assert message == plaintext, "The encryption-decryption loop doesn't close."