import socket
import threading

from Crypto.Cipher.AES import AESCipher
from Crypto.PublicKey import RSA
from base64 import b64decode


# from base64 import b64encode
class Client(threading.Thread):

    __publicKey = ""
    __privateKey = ""
    __sock2serv = ""
    __sessionKey = ""

    # generates a public/private keypair
    def generateKey(self,bits=1024):
        rsaObject = RSA.generate(bits)
        self.__publicKey = rsaObject.publickey().exportKey("PEM")
        self.__privateKey = rsaObject.exportKey("PEM")


    def encrypt(self, message) :
        cipher = AESCipher.__init__(self, self.__sessionKey)
        encrypted = cipher.encrypt(message)
        return encrypted.encode('base64')

    def decrypt(self, message) :
        cipher = AESCipher.__init__(self, self.__sessionKey)
        decryptedMessage = cipher.decrypt(b64decode(message))
        return decryptedMessage
    
    def 
        
