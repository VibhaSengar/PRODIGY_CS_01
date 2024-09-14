# PRODIGY_CS_01
The task is to create a simple Caesar Cipher tool in Python that can both encrypt and decrypt text messages based on a user-specified shift value. The Caesar Cipher is a basic substitution cipher where each letter in the plaintext is shifted by a certain number of positions (the shift value) in the alphabet. 
Understanding the Code
The provided Python code accomplishes this task by allowing the user to:

Choose to Encrypt or Decrypt a message.
Enter the message they want to encrypt or decrypt.
Enter the shift value, which defines how many positions each letter should be shifted.
1. The encrypt Function
This function takes two inputs:

text: The message to be encrypted.
shift: The number of positions each character in the text will be shifted.
For each character in the text, the function checks if it is:

Uppercase Letter: If the character is uppercase (A-Z), it converts the character to its ASCII value using ord(), shifts it using the provided shift value, and then converts it back to a character using chr(). The result is wrapped around the alphabet if the shift moves beyond Z.

Lowercase Letter: Similarly, for lowercase letters (a-z), the same process is applied, but with ASCII values of lowercase letters.

Non-Letter Characters: If the character is not a letter (such as punctuation or space), it is left unchanged.

Example of the Encryption Logic:
If the text is "HELLO" and the shift value is 3, the cipher shifts each letter by 3 positions in the alphabet:
H becomes K
E becomes H
L becomes O
O becomes R
Thus, "HELLO" becomes "KHOOR".

2. The decrypt Function
This function reverses the encryption by shifting the letters back by the given shift value.

For each character in the text, the function:

Shifts Uppercase Letters Back: For each uppercase letter, the ASCII value is shifted in the opposite direction (backward) by the shift value, and the result is wrapped around if necessary.

Shifts Lowercase Letters Back: The same process is applied to lowercase letters.

Leaves Non-Letters Unchanged: Non-letter characters remain as they are.

3. The main Function
The main() function is the starting point of the program. It prompts the user to:

Choose between encryption or decryption: The user enters either e (for encryption) or d (for decryption).

Input the message: The user provides the message they want to encrypt or decrypt.

Input the shift value: The user provides a number that will determine how far the letters should be shifted in the alphabet.

Depending on the user's choice:

If they choose to encrypt, the encrypt() function is called with the message and shift value.
If they choose to decrypt, the decrypt() function is called instead.
Finally, the program prints out the encrypted or decrypted message.

Summary
This code provides a clear and simple implementation of the Caesar Cipher, allowing users to encrypt and decrypt messages using a shift-based substitution algorithm.
