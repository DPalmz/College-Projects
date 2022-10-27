from random import randint
from Crypto.PublicKey import RSA

key = RSA.generate(bits=1024, e=3)
e = key.e
n = key.n

m = randint(0, 999)
print(m)
c = m**e % n 

hack = c**(1/e)
print(hack)
