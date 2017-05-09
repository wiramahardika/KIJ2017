import random
import string
from fractions import gcd

MIN_RANDOM = 255
MAX_RANDOM = 1000

def generatePrime():
    while True:
        p = random.randrange(MIN_RANDOM, MAX_RANDOM, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def randomE(m):
    while True:
        e = random.randint(MIN_RANDOM, MAX_RANDOM)
        if e > 2 and m % e != 0:
            return e

def findCoPrime(m):
    while True:
        e = randomE(m)
        if gcd(m, e) == 1:
            return e

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encrypt(plain_text, public_key):
    chiper = []
    e = public_key[0]
    n = public_key[1]
    for i in range(0, len(plain_text)):
        t = ord(plain_text[i])
        chiper.append(pow(t, e) % n)
    return chiper

def decrypt(chiper, private_key):
    plain_text = ''
    d = private_key[0]
    n = private_key[1]
    for i in range(0, len(chiper)):
        t = pow(chiper[i], d) % n
        plain_text += str(unichr(t))
    return plain_text

def generateDESkey():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

def generateKey():
    p = generatePrime()
    print 'p = '+str(p)
    q = generatePrime()
    print 'q = '+str(q)
    n = p * q
    print 'n = '+str(n)
    m = (p-1) * (q-1)
    print 'm = '+str(m)
    e = findCoPrime(m)
    print 'e = '+str(e)
    d = modinv(e, m)
    print 'd = '+str(d)

    public_key = [e, n]
    private_key = [d, n]
    return {'public': public_key, 'private': private_key}

# chiper =  encrypt('CELAK gembrong berbulu lebat', public_key)
# print chiper
# plain_text = decrypt(chiper, private_key)
# print plain_text