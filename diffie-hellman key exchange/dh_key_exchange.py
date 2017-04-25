import random

def generateLargePrime():
    while True:
        p = random.randrange(1000, 9999, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def generateSmallPrime():
    while True:
        p = random.randrange(20, 999, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def count_public_key(prime_number, g, n):
    return pow(g, prime_number) % n

def count_private_key(public_key, prime_number, n):
    return pow(public_key, prime_number) % n

def set_key(private_key):
    key = 'kij'
    for i in range(0, 5-len(private_key)):
        key = key+'0'
    return key+private_key