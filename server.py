from base64 import b64decode
import socket
import threading
import string
import random

from Crypto.Cipher.AES import AESCipher


class Server(threading.Thread):

    sessionKey = ""

    def genSessionKey(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

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
        server_address = ('localhost', 10000)
        sock.bind(server_address)

        while active:
            connection, client_address = sock.accept()
            print "waiting for connection"

            try:
                print "connection from", client_address

                while True:
                    data = connection.recv(16)
                    print "received '%s'" % data
                    if data.startswith("!key"):
                        if data:
                            print "sending session key to the client"
                            connection.sendall("test") #TODO: generate session key and encrypt it with the received private key
                        else:
                            print "no more data from", client_address
                            break
                    elif data.startswith("!crypt"):
                        pass
                    elif data.startswith("!plain"):
                        pass
                    else:
                        pass
            
            finally:
                connection.close()


def main():
    s = Server()
    s.start()

if __name__ == '__main__':
    main()

