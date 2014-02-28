# from base64 import b64encode
from M2Crypto import RSA  
# import os          

def generateKey():
    key = RSA.gen_key(1024, 65537)
    key.save_key("my.key", cipher=None)
    key.save_pub_key("my.key.pub")
    
    # raw_key = key.pub()[1]
    # b64key = b64encode(raw_key)

    # username = os.getlogin()
    # hostname = os.uname()[1]
    # keystring = 'ssh-rsa %s %s@%s' % (b64key, username, hostname)

    # with open(os.getenv('HOME')+'/.ssh/id_rsa.pub') as keyfile:
    #     keyfile.write(keystring)

def main():
    print generateKey()

if __name__ == '__main__':
    main()