import socket
import json

import sys

from des_encrypt import *
from dh_key_exchange import *

s1 = socket.socket()
host = socket.gethostbyname(socket.gethostname())
print '* Masukkan port'
print '>',
port = int(raw_input())
s1.bind((host, port))

g = generateLargePrime()
n = generateSmallPrime()
print '\n* Nilai g = '+str(g)+', dan nilai n = '+str(n)

print '* Alamat IP anda:', host
print '* Menunggu user2 terhubung...'
s1.listen(5)

s2, addr = s1.accept()
print '* Anda terhubung dengan user2 dengan alamat ', addr
print '* Mengirim nilai g dan n ke user2...'
s2.send(json.dumps({'g': g, 'n': n}))
response = s2.recv(1024)
if response == 'OK':
    print '* Nilai g dan n terkirim!'
else:
    print '* Gagal mengirim nilai g dan n!'
    s2.close()
    sys.exit(0)

random_prime = generateLargePrime()
public_key = count_public_key(random_prime, g, n)
print '* Public Key anda adalah ' + str(public_key)

print '* Mengirim public key anda ke user2...'
s2.send(str(public_key))

print '* Menunggu public key dari user2...'
public_key_user2 = int(s2.recv(1024))
print '* Public Key user2 adalah '+str(public_key_user2)

print '* Menghitung private key...'
private_key = count_private_key(public_key_user2, random_prime, n)
print '* Private Key = '+str(private_key)
key = set_key(str(private_key))
print '* Key = '+key

print '* \n\nObrolan dimulai!\n\n'

while True:
    print '>',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg, key)
    s2.send(encrypted_msg)
    reply_msg = ofb_decrypt(a, s2.recv(1024))
    print 'user2: ', reply_msg

s2.close()