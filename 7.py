p_sofar = [2]
p = 3
i = 1
limit = 543+3

def is_prime(x, p_sofar):
    for p in p_sofar:
        if x % p == 0:
            return False
    return True

while i < limit:
    if is_prime(p, p_sofar):
        i += 1
        p_sofar.append(p)
    p += 2 # don't need to test even numbers
        
print p_sofar[3:]
print len(p_sofar[3:])
print sum(p_sofar[3:])
