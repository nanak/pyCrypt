import socket
import threading

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from base64 import b64decode
from sys import argv
from sys import exit
import sys
# from logilab.common.shellutils import RawInput


# from base64 import b64encode
class Client(threading.Thread):

    publicKey = ""
    privateKey = ""
    sock2serv = ""
    sessionKey = ""
    block_size = 32

    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
    unpad = lambda s : s[0:-ord(s[-1])]

    # generates a public/private keypair
    def generateKey(self, bits=1024):
        rsaObject = RSA.generate(bits)
        self.publicKey = rsaObject.publickey().exportKey("PEM")
        self.privateKey = rsaObject.exportKey("PEM")

    # encryptes the message with AES
    # cipher-text is the sessionkey
    def encrypt(self, message) :
        print "encryptedMuh"
        cipher = AES.new(self.sessionKey, AES.MODE_CBC, 'This is an IV456')
        print "encMuh2"
        encrypted = cipher.encrypt(pad(message))
        print "muh3"
        message = encrypted.encode('base64')
        print message
        return message

    # decryptes the message with AES
    # cipher-text is the sessionkey
    def decrypt(self, message) :
        cipher = AESCipher.__init__(self.sessionKey)
        decryptedMessage = cipher.decrypt(b64decode(message))
        return decryptedMessage
    
    # decryptes the session key which is reveived from the server
    # decryption is done with private-key (RSA)
    def decryptSessionKey(self, sessionKeyEncrypted):
        rsakey = RSA.importKey(self.privateKey)
        # raw_cipher_data = b64decode(sessionKeyEncrypted)
        decrypted = rsakey.decrypt(sessionKeyEncrypted)
        return decrypted        
    
    # define the behaviour for the thread
    def run(self):
        # if(len(argv) >= 3):
        try:
            if True:
                active = True
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # server_address = (argv[1], argv[2])
                server_address = ("127.0.0.1", 10000)
                # sock.bind(server_address)
                sock.connect(server_address)
                # print "Connection established to: \n" + argv[1] + ":" + argv[2]
                print "Connection established to: \n" + "127.0.0.1" + ":" + "10000"
                self.generateKey()
                print "Public and Private-key generation successful! \n"
                # sock.send("!key%s"  % self.publicKey)
                sock.send("!key " + self.publicKey)
                print "Public-key sent to server, waiting for session-key ... \n"
                firstMessage = sock.recv(1024)
                print firstMessage
                self.sessionKey = self.decryptSessionKey(firstMessage)
                print "Session-key was decrypted successfully: " + self.sessionKey
                goOn = True
                while goOn:
                    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    #connection, connection_address = sock.accept()
                    try:
                        while goOn:
                            command = raw_input("Message: ")
                            print command
                            command = command.lower().split(' ', 1)
                            print command
                            if len(command) > 1:
                                ctrl = command[0]
                                message = command[1]
                            else:
                                ctrl = ""
                                message = command[0]
                            if (ctrl == "!crypt"):
                                print "muh123"
                                encryptedMessage = self.encrypt(message)
                                print "muuuuh"
                                sock.send(encryptedMessage)
                                print "muh321"
                            elif (ctrl == "!exit"):
                                goOn = False
                            else:
                                print "muh"
                                sock.send(message)
                            data = sock.recv(1024)
                            if data:
                                print "Received: \n '%s'" % data
                            else:
                                print "no more data from", client_address
                        # elif data.startswith("!crypt"):
                        #     pass
                        # elif data.startswith("!plain"):
                        #     pass
                        # else:
                        #     pass
                
                    finally:
                        sock.close()
        except:
            print "any exception ", sys.exc_info()[0]
    # elif :
    #     print "Please enter the server ip and port as 2 separate parameters and restart the programm! \n"

def main():
    c = Client()
    c.start()
    # pass
    
if __name__ == '__main__':
    main() 
