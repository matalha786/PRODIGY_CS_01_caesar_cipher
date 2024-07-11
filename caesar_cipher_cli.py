def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not a letter, leave it as is
        else:
            result += char

    return result

def main():
    previous_encrypted = None

    while True:
        print("\nCaesar Cipher Program")
        print("Press 1 to Encrypt")
        print("Press 2 to Decrypt")
        print("Press 3 to Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            mode = 'encrypt'
            message = input("Enter your message: ")
            shift = int(input("Enter shift value: "))
            result = caesar_cipher(message, shift, mode)
            print(f"Result: {result}")
            previous_encrypted = result

        elif choice == '2':
            if previous_encrypted:
                decrypt_previous = input("Do you want to decrypt the previous encrypted message? (y/n): ").strip().lower()
                if decrypt_previous == 'y':
                    mode = 'decrypt'
                    shift = int(input("Enter shift value: "))
                    result = caesar_cipher(previous_encrypted, shift, mode)
                    print(f"Result: {result}")
                else:
                    message = input("Enter your message: ")
                    shift = int(input("Enter shift value: "))
                    result = caesar_cipher(message, shift, mode='decrypt')
                    print(f"Result: {result}")
            else:
                message = input("Enter your message: ")
                shift = int(input("Enter shift value: "))
                result = caesar_cipher(message, shift, mode='decrypt')
                print(f"Result: {result}")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose '1', '2', or '3'.")

if __name__ == "__main__":
    main()
