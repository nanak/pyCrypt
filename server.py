from base64 import b64decode
import socket
import threading
import string
import random

from Crypto.Cipher.AES import AESCipher
from Crypto.PublicKey import RSA


# socket tut: http://pymotw.com/2/socket/tcp.html

class Server(threading.Thread):

    sessionKey = ""

    def genSessionKey(self, size=32, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    # def encryptSessionKey(self, publicKey, sessionKey):
    #     rsaObjectImpl = RSA.RSAImplementation.importKey(publicKey)
    #     rsaObject = RSA._RSAobj.__init__(rsaObjectImpl, publicKey)
    #     return rsaObject.encrypt(sessionKey)

    def encryptSessionKey(self, sessionKey, publicKey):
        rsakey = RSA.importKey(publicKey)
        # raw_cipher_data = b64decode(sessionKey)
        encrypted = rsakey.encrypt(sessionKey, "muh")
        return encrypted     
    

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
    
    # define the behaviour for the thread
    def run(self):
        active = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.1', 10000)
        sock.bind(server_address)
        # Listen for incoming connections
        sock.listen(1)

        while active:
            print "waiting for connection"
            connection, client_address = sock.accept()

            try:
                print "connection from", client_address

                while True:
                    data = connection.recv(1024)
                    print "received '%s'" % data
                    cache =  data.split(" ", 1)
                    print cache[0]
                    if cache[0] == "!key":
                        if data:
                            print "sending session key to the client"
                            print len(cache)
                            sessionKeyy=self.genSessionKey()
                            print sessionKeyy
                            message = self.encryptSessionKey(sessionKeyy, cache[1])
                            print self.sessionKey
                            connection.sendall(message[0])
                            # break
                        else:
                            print "no more data from", client_address
                            # break
                    elif data.startswith("!crypt"):
                        print "muh"
                    else:
                        pass
            
            finally:
                connection.close()


def main():
    s = Server()
    s.start()

if __name__ == '__main__':
    main()

