from des_encrypt import *
import socket

s = socket.socket()
port = 14091

print '* Masukkan alamat IP server'
print '>',
host = raw_input()

print '\n* Menguhubngkan ke server...'
s.connect((host, port))
print '* Anda sudah terhubung!\n\n'

while True:
    a = s.recv(1024)
    print a
    reply_msg = ofb_decrypt(a)
    print 'Sender: ', reply_msg
    print '> ',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg)
    s.send(encrypted_msg)

s.close