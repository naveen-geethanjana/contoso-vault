message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext: str = ""
for letter in message:
    if ord("A") <= ord(letter) <= ord("Z"):
        print("A" <= letter <= "Z")
    else:
        print("FALSE")
    ciphertext_letter = chr((ord(letter) + key))
    ciphertext += ciphertext_letter

print(ciphertext)