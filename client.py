import socket
import threading

from Crypto.Cipher.AES import AESCipher
from Crypto.PublicKey import RSA
from base64 import b64decode


# from base64 import b64encode
class Client(threading.Thread):

    publicKey = ""
    privateKey = ""
    sock2serv = ""
    sessionKey = ""

    # generates a public/private keypair
    def generateKey(self,bits=1024):
        rsaObject = RSA.generate(bits)
        self.publicKey = rsaObject.publickey().exportKey("PEM")
        self.privateKey = rsaObject.exportKey("PEM")

    # encryptes the message with AES
    # cipher-text is the sessionkey
    def encrypt(self, message) :
        cipher = AESCipher.__init__(self, self.sessionKey)
        encrypted = cipher.encrypt(message)
        return encrypted.encode('base64')

    # decryptes the message with AES
    # cipher-text is the sessionkey
    def decrypt(self, message) :
        cipher = AESCipher.__init__(self, self.sessionKey)
        decryptedMessage = cipher.decrypt(b64decode(message))
        return decryptedMessage
    
    def main(self):
        
    
    if__name__='__main__':
        main() 
