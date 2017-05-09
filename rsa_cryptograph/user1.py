import socket
import json
from rsa import *
from des_encrypt import *


s1 = socket.socket()
host = socket.gethostbyname(socket.gethostname())
print '* Masukkan port'
print '>',
port = int(raw_input())
s1.bind((host, port))

print '* Alamat IP anda:', host
print '* Menunggu user2 terhubung...'
s1.listen(5)

s2, addr = s1.accept()
print '* Anda terhubung dengan user2 dengan alamat ', addr

print '* Menyiapkan key...'
key = generateKey()

print '\n* Public Key: '+str(key['public'])
print '* Private Key: '+str(key['private'])

print '\n* Mengirim public key ke user2...'
s2.send(json.dumps(key['public']))

print '* Menunggu DES key dari user2...'
des_key_encrypted = json.loads(s2.recv(1024))
# print s2.recv(1024)
print '* DES key diterima'

print '* Dekripsi DES key...'
des_key = decrypt(des_key_encrypted, key['private'])
print '* DES key:'+des_key
s2.send('OK')


print '\n\n* Obrolan dimulai!\n\n'
while True:
    received_msg_plain = s2.recv(1024)
    received_msg_decrypted = ofb_decrypt(received_msg_plain, des_key)
    print '\nuser2 (plain): ', received_msg_plain
    print 'user2 (decrypted): ', received_msg_decrypted
    print '> ',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg, des_key)
    s2.send(encrypted_msg)

s2.close()