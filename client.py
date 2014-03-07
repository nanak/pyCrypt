import socket
import threading

from Crypto.Cipher.AES import AESCipher
from Crypto.PublicKey import RSA
from base64 import b64decode
from sys import argv
from sys import exit
# from logilab.common.shellutils import RawInput


# from base64 import b64encode
class Client(threading.Thread):

    publicKey = ""
    privateKey = ""
    sock2serv = ""
    sessionKey = ""

    # generates a public/private keypair
    def generateKey(self, bits=1024):
        rsaObject = RSA.generate(bits)
        self.publicKey = rsaObject.publickey().exportKey("PEM")
        self.privateKey = rsaObject.exportKey("PEM")

    # encryptes the message with AES
    # cipher-text is the sessionkey
    def encrypt(self, message) :
        cipher = AESCipher.__init__(self.sessionKey)
        encrypted = cipher.encrypt(message)
        return encrypted.encode('base64')

    # decryptes the message with AES
    # cipher-text is the sessionkey
    def decrypt(self, message) :
        cipher = AESCipher.__init__(self.sessionKey)
        decryptedMessage = cipher.decrypt(b64decode(message))
        return decryptedMessage
    
    # decryptes the session key which is reveived from the server
    # decryption is done with private-key (RSA)
    def decryptSessionKey(self, sessionKeyEncrypted):
        rsaObjectImpl = RSA.RSAImplementation.__init__()
        rsaObjectImpl.importKey(self.publicKey)
        rsaObject = RSA._RSAobj.__init__(rsaObjectImpl, self.privateKey)
        self.sessionKey = rsaObject.decrypt(sessionKeyEncrypted)        
    
    # define the behaviour for the thread
    def run(self):
        # if(len(argv) >= 3):
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
            sock.send(self.publicKey)
            print "Public-key sent to server, waiting for session-key ... \n"
            firstMessage = sock.recv(1024)
            print firstMessage
            self.decryptSessionKey(firstMessage)
            print "Session-key was decrypted successfully: " + self.sessionKey
        
            while active:
                try:
                    # command = raw_input("Message: ")
                    command = "test"
                    command = command.lower().split(' ', 1)
                    ctrl = command.pop(0);
                    message = command.pop(0)
                    if (ctrl is "!encrypt"):
                        encryptedMessage = self.encrypt(message)
                        sock.send(encryptedMessage)
                    elif (ctrl is "!plain"):
                        sock.send(message)
                    data = connection.recv(1024)
                    print "received '%s'" % data
                    if data.startswith("!key"):
                        if data:
                            print "sending session key to the client"
                            connection.sendall("test")  # TODO: generate session key and encrypt it with the received private key
                    else:
                            print "no more data from", client_address
                            break
                    # elif data.startswith("!crypt"):
                    #     pass
                    # elif data.startswith("!plain"):
                    #     pass
                    # else:
                    #     pass
            
                finally:
                    connection.close()
                    exit()
    # elif :
    #     print "Please enter the server ip and port as 2 separate parameters and restart the programm! \n"

def main():
    c = Client()
    c.start()
    # pass
    
if __name__ == '__main__':
    main() 
