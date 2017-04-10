import socket
from des_encrypt import *

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 14021
s.bind((host, port))

print '* Alamat IP Server:', socket.gethostbyname(socket.gethostname())
print '* Menunggu client terhubung...'
s.listen(5)
c, addr = s.accept()
print '* Anda terhubung dengan client dengan alamat ', addr
print '* Obrolan dimulai\n\n'

while True:
    print '>',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg)
    c.send(encrypted_msg)
    reply_msg = ofb_decrypt(c.recv(1024))
    print 'Client: ', reply_msg
    #print encrypted_msg

c.close()

#socket = pintu akses data
#kunci masuk socket host dan port nya server
#isinya c dan addr sama


#recv dan send = tujuan
#accept dan listen = diri sendiri