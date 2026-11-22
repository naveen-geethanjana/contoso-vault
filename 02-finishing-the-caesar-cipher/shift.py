ALPHABET_SIZE = 26

message: str = input("Message: ")  # "AB$78"
key: int = int(input("Key: "))

ciphertext: str = ""

for letter in message:
    if "A" <= letter<= 'Z':
        shifted = ord(letter) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    else:
        ciphertext += letter

print("Ciphertext:", ciphertext)

plaintext: str = ""

for letter in ciphertext:
    if "A" <= letter<= 'Z':
        shifted = ord(letter) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += letter

print("Plaintext:", plaintext)

assert message == plaintext, "The encryption-decryption loop doesn't close."
