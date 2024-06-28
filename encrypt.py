#Practice code to see if symmetric encryption/decryption methods are performing correctly

#Import cryptography, a package designed to expose cryptographic primitives and recipes to Python developers.
import cryptography
#From the cryptography package, import Fernet, a symmetric key encryption algorithm that uses 256-bit keys to encrypt and decrypt data.
from cryptography.fernet import Fernet

#Message to be encrypted/decrypted
message = "hello geeksters"

#Generate a key to be used for the encryption/decryption
##Using Fernet to generate the key
key = Fernet.generate_key()

#Instance the Fernet class with the key generated above
fernet = Fernet(key)

#Use the Fernet class instance to encrypt the message above
##Message has to be encoded to byte string before encryption takes place
enc_message = fernet.encrypt(message.encode())

#Prints the original message instantiated above
print("Original String: ", message)
#Prints the original message after encryption
print("Encrypted String: ", enc_message)

#Use the Fernet class instance to decrypt the encrypted message above
##Message was encoded, so it has to be decoded to return back to its original form
dec_message = fernet.decrypt(enc_message).decode()

#Prints the encrypted message after being decrypted
print("Decrypted String: ", dec_message)