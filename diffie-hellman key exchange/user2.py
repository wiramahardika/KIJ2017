from des_encrypt import *
import socket
import json
from dh_key_exchange import *

s1 = socket.socket()

print '* Masukkan alamat IP user1'
print '>',
host = raw_input()
print '* Masukkan port user1'
print '>',
port = int(raw_input())

print '\n* Menguhubngkan ke user1...'
s1.connect((host, port))
print '* Anda sudah terhubung!\n\n'

print '* Menunggu nilai g dan n dari user1...'
response = json.loads(s1.recv(1024))
g = response['g']
n = response['n']
print '* Nilai g = '+str(g)+', dan nilai n = '+str(n)
s1.send('OK')

random_prime = generateLargePrime()
public_key = count_public_key(random_prime, g, n)

print '* Public Key anda adalah '+str(public_key)

print '* Menunggu public key dari user1...'
public_key_user1 = int(s1.recv(1024))
print '* Public Key user1 adalah '+str(public_key_user1)

print '* Mengirim public key anda ke user2...'
s1.send(str(public_key))

print '* Menghitung private key...'

private_key = count_private_key(public_key_user1, random_prime, n)

print '* Private Key = '+str(private_key)
key = set_key(str(private_key))
print '* Key = '+key

print '* \n\nObrolan dimulai!\n\n'

while True:
    reply_msg = ofb_decrypt(s1.recv(1024), key)
    print 'user1: ', reply_msg
    print '> ',
    msg = raw_input()
    encrypted_msg = ofb_encrypt(msg, key)
    s1.send(encrypted_msg)

s1.close
