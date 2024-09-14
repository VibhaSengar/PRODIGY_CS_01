def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around if necessary
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            encrypted_text += new_char
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around if necessary
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            # If it's not a letter, keep it as is
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift the character back and wrap around if necessary
            new_char = chr((ord(char) - shift - 65) % 26 + 65)
            decrypted_text += new_char
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift the character back and wrap around if necessary
            new_char = chr((ord(char) - shift - 97) % 26 + 97)
            decrypted_text += new_char
        else:
            # If it's not a letter, keep it as is
            decrypted_text += char

    return decrypted_text


def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ").lower()

    if choice in ['e', 'encrypt']:
        text = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(text, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice in ['d', 'decrypt']:
        text = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(text, shift)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid choice, please choose 'e' for encryption or 'd' for decryption.")


# Run the program
if __name__ == "__main__":
    main()
