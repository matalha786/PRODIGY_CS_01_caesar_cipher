# PRODIGY_CS_01_caesar_cipher
# Caesar Cipher Program

This is a GUI-based Caesar Cipher program that allows you to encrypt and decrypt messages using a simple shift-based substitution cipher. The program is built using Python and the `tkinter` library.

## Features

- Encrypt messages using the Caesar Cipher algorithm
- Decrypt messages using the Caesar Cipher algorithm
- User-friendly GUI with separate sections for encryption and decryption
- Option to decrypt the previously encrypted message
- Scalable and adjustable window layout

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone github.com/matalha786/PRODIGY_CS_01_caesar_cipher
   ```

2. Navigate to the project directory:

   ```bash
   cd caesar-cipher-tool
   ```

3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. install requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```
   
   OR
    
5. Install the required libraries directly (if not already installed):

   ```bash
   pip install tk
   ```

## Usage

1. Run the `caesar_cipher_gui.py` file:

   ```bash
   python caesar_cipher_gui.py
   ```

2. Use the GUI to:
   - Enter your message in the encryption section and provide a shift value, then click "Encrypt" to see the encrypted result.
   - Enter your message in the decryption section and provide a shift value, then click "Decrypt" to see the decrypted result.
   - Optionally, decrypt the previously encrypted message by clicking "Decrypt" in the decryption section and choosing to decrypt the last encrypted message.

## GUI Layout

- **Encryption Section**:
  - Enter your message to encrypt
  - Enter the shift value for encryption
  - Click the "Encrypt" button to see the encrypted result

- **Decryption Section**:
  - Enter your message to decrypt
  - Enter the shift value for decryption
  - Click the "Decrypt" button to see the decrypted result
  - Optionally decrypt the last encrypted message

- **Exit**:
  - Click the "Exit" button to close the program

## Example

### Encryption

1. Enter your message: `Hello, World!`
2. Enter shift value: `3`
3. Click "Encrypt"
4. Encrypted Result: `Khoor, Zruog!`

### Decryption

1. Enter your message: `Khoor, Zruog!`
2. Enter shift value: `3`
3. Click "Decrypt"
4. Decrypted Result: `Hello, World!`



## License

This project is licensed under the GLP License - see the [LICENSE](LICENSE) file for details.
