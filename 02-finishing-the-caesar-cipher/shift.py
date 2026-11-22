ALPHABET_SIZE = 26

message: str = input("Message: ")  # "AB$78"
key: int = int(input("Key: "))

ciphertext: str = ""

# What if the message had symbols to begin with?
# What if the message has lowercase letters?

for letter in message:
    if "A" <= letter<= 'Z':
        shifted = ord(letter) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    else:
        ciphertext += letter

plaintext: str = ""

for letter in ciphertext:
    if "A" <= letter<= 'Z':
        shifted = ord(letter) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += letter

print(plaintext)
