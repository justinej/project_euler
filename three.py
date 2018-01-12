
def smallest_divisor(x):
    for divisor in xrange(2, x+1):
        if x % divisor == 0:
            return divisor
def is_prime(x):
    assert(x>1)
    return smallest_divisor(x) == x

def find_largest_pf(x):
    while x > 1:
        if is_prime(x):
            return x
        else: x = x/smallest_divisor(x)

# base = 600851475143
#print find_largest_pf(base)
