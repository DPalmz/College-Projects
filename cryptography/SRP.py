from cmath import nan
from operator import mod
import sympy
import gmpy2
import pickle

    
p = sympy.randprime(0, 999)
q = sympy.randprime(0, 999)
n = p*q
e = 17
et = (p-1)*(q-1)
#print(et)
    
test = pow(17, -1, 3120)    
    
d = pow(e, -1,  et)
c = 0
m = 42

c = m**e % n 
print(c)
  

m = (c**d) % n
print(m)

#m = b"this is a message"

c = m**e % n 
print(c)
  

m = (c**d) % n
#m = str(m)
print(m)




        
            
            
        
        

