import socket
import threading
from M2Crypto import RSA

class Server(threading.Thread):

    # generate session key
    def genSessionKey(self):
        pass


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

