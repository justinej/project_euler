def is_prime(x, p_sofar):
    for p in p_sofar:
        if x % p == 0:
            return False
    return True

p_sofar = [2]
i = 3
while i < 2*(10**6):
    if is_prime(i, p_sofar):
        p_sofar.append(i)
    i += 2 # don't need to test even numbers
    if (i-1)%10**4 == 0:
        print i

print len(p_sofar)
print sum(p_sofar)
