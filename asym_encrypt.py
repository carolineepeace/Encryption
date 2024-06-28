#Practice code to see if asymmetric encryption/decryption methods are performing correctly

#Import rsa, a library that provides functions for generating public and private keys, encrypting and decrypting data, and signing and verifying signatures.
import rsa

#Generate public and private keys using the rsa library functions
pubKey, privKey = rsa.newkeys(512)

#Message to be encrypted/decrypted
message = "hello geeksters"

#Use the rsa library to encrypt the original message with the public key
##Message has to be encoded to byte string before encryption takes place
enc_message = rsa.encrypt(message.encode(), pubKey)

#Prints the original message instantiated above
print("Original String: ", message)
#Prints the original message after encryption
print("Encrypted String: ", enc_message)

#Use the rsa library to decrypt the encrypted message above with the private key
##Message was encoded, so it has to be decoded to return back to its original form
dec_message = rsa.decrypt(enc_message, privKey).decode()

#Prints the encrypted message after being decrypted
print("Decrypted String: ", dec_message)