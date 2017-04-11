from des_encrypt import *
import socket

s = socket.socket()

print '* Masukkan alamat IP server'
print '>',
host = raw_input()
print '* Masukkan port server'
print '>',
port = int(raw_input())

print '\n* Menguhubngkan ke server...'
s.connect((host, port))
print '* Anda sudah terhubung!\n\n'

while True:
    reply_msg = ofb_decrypt(s.recv(1024))
    print 'Sender: ', reply_msg
    print '> ',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg)
    s.send(encrypted_msg)

s.close