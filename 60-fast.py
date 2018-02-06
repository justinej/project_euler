# solution from the website
# Euler 60
from time import time
start = time()
from 60 import primes # Finds all prime numbers less than n
lst=primes(10000)

def isprime(n):
    for d in lst:
        if n%d==0 and d*d<=n:
            return False
        if d*d>n:
            return True
    
def p(x,y):
    if isprime(int(str(x)+str(y))) and isprime(int(str(y)+str(x))):
        return True
    else:
        return False

ans=(sum((a,b,c,d,e))
     for a in lst
     for b in lst
         if a<b and p(a,b)
     for c in lst
         if b<c and p(a,c) and p(b,c)
     for d in lst
         if c<d and p(a,d) and p(b,d) and p(c,d)
     for e in lst
         if d<e and p(a,e) and p(b,e) and p(c,e) and p(d,e))

def euler60():
    for n in ans:
        print('Answer: ',n)
        break

euler60()
print('Time: ',time()-start)
