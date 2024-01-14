alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text: str, shift: int):
        cipher = []
        for c in text:
            index = alphabet.index(c)  
            index += shift
            if index >= len(alphabet) - 1:
                index = index - (len(alphabet))
            cipher.append(alphabet[index])
        print(f"The endoded text is {''.join(cipher)}")

    def decrypt(text: str, shift: int):
        decoded = []
        for c in text:
            index = alphabet.index(c) - shift       
            decoded.append(alphabet[index])
        print(f"The decoded text is {''.join(decoded)}")

    if direction.lower() == "encode":
        encrypt(text, shift)
    elif direction.lower() == "decode":
        decrypt(text, shift)
    else:
        print("That's not an option, try again...")
        continue

    continue_cipher = input("Do you want to continue? Y/n\n> ")
    if(continue_cipher.lower() != 'y'):
        break
