import socket
import json
from rsa import *
import sys
from des_encrypt import *


s1 = socket.socket()

print '* Masukkan alamat IP user1'
print '>',
host = raw_input()
print '* Masukkan port user1'
print '>',
port = int(raw_input())

print '\n* Menyiapkan DES key...'
des_key = generateDESkey()
print '* DES Key: '+str(des_key)

print '\n* Menguhubngkan ke user1...'
s1.connect((host, port))
print '* Anda sudah terhubung!\n\n'

print '\n* Menunggu public key dari user1...'
public_key = json.loads(s1.recv(1024))
print '* Diterima! Public Key: '+str(public_key)

print '* Enkripsi DES key...'
des_key_encrypted = encrypt(des_key, public_key)
print '* DES key telah dienkripsi, mengirim DES key ke user2...'
s1.send(json.dumps(des_key_encrypted))
# s1.send('test')
if s1.recv(1024) == 'OK':
    print '* Transaksi DES key selesai!'
else:
    print '* Gagal mengirim public key'
    s1.close()
    sys.exit(0)


print '\n\n* Obrolan dimulai!\n\n'
while True:
    print '\n>',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg, des_key)
    s1.send(encrypted_msg)
    received_msg_plain = s1.recv(1024)
    received_msg_decrypted = ofb_decrypt(received_msg_plain, des_key)
    print 'user1 (plain): ', received_msg_plain
    print 'user1 (decrypted): ', received_msg_decrypted

s1.close()
