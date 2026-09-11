# This program demonstrates the use of the cryptography library to encrypt and decrypt a message.
# Name: Dustin Lopera
# Date: September 11, 2026

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"Hello, World!") # b is a byte string (encoding) to be encryped/decrypted.
print("Encoded:", encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print ("Decoded:", decoded_text.decode()) # decode() converts the byte string back to a regular string.

