import socket
import threading
# from base64 import b64encode
from M2Crypto import RSA

keyFilename = "my.key"
pubKeyFilename = "my.key.pub"

class Client(threading.Thread):

    # generates a public/private keypair
    def generateKey(self):
        key = RSA.gen_key(1024, 65537)
        key.save_key(keyFilename, cipher=None)
        key.save_pub_key(pubKeyFilename)
        # raw_key = key.pub()[1]
        # b64key = b64encode(raw_key)

        # username = os.getlogin()
        # hostname = os.uname()[1]
        # keystring = 'ssh-rsa %s %s@%s' % (b64key, username, hostname)

        # with open(os.getenv('HOME')+'/.ssh/id_rsa.pub') as keyfile:
        #     keyfile.write(keystring)

    # read a file and return it as string
    def readFile(self, filename):
        return open(filename, 'r').read()