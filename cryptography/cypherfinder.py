
from random import randint
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

key = RSA.generate(bits=1024)
N = key.n
E = key.e
S = randint(1, 999)
M = 32
C = M**E % N 

#hash = SHA256.new(C)

CC = ((S**E % N)* C) % N
temp = (CC/S)
P = pow(temp, -1, N)
print(P)