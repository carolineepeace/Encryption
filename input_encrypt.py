#Takes user input then uses symmetric encryption on the input and performs decryption to reveal the original input

#Import cryptography, a package designed to expose cryptographic primitives and recipes to Python developers.
import cryptography
#From the cryptography package, import Fernet, a symmetric key encryption algorithm that uses 256-bit keys to encrypt and decrypt data.
from cryptography.fernet import Fernet

#Generates key for encryption & instantiates the Fernet class with the key
key = Fernet.generate_key()
fernet = Fernet(key)

#Get input from user for message to be encrypted
message = input("Enter the message you want encrypted: ")
#Encrypts the message input from user
##Encodes the message so it can be encrypted
encrypt_message = fernet.encrypt(message.encode())
#Decrypts the encrypted message from above
##Decodes the message so it can be decrypted
decrypt_message = fernet.decrypt(encrypt_message).decode()

#Creates and opens file to log the user's original message
with open("encryptions.txt", "a") as file:
    file.write(f"Original Message: {message}\n")
    file.write(f"Encrypted Message: {encrypt_message.decode()}\n")
    file.write(f"Decrypted Message: {decrypt_message}\n\n")
    file.close()

#Opens the file to log the encrypted version of the user's message
#Prints the message before and after encryption
print("Message before encryption: ", message)
print("Message after encryption: ", encrypt_message)
#Prints the message back after the encrypted message was decrypted
print("Message after decryption: ", decrypt_message)