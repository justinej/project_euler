UPPER_LIMIT = 10**2

def is_prime(x, primes):
    if x in primes:
        return True
    for p in primes:
        if x%p==0:
            return False
    return True

def all_primes(x):
    # Finds all primes under x
    p_sofar = []
    for i in xrange(2, x):
        if is_prime(i, p_sofar):
            p_sofar.append(i)
        if i%10**4 == 0:
            print "step {} out of {}".format(i, x)
    return p_sofar

all_primes = all_primes(UPPER_LIMIT)
print "done caluculating all primes"

def longest_seq(y):
    # Longest sequence that sums to a prime
    # that starts with the y-th prime
    seq = [all_primes[y]]
    total = sum(seq)
    #print "seq is...{}".format(seq)
    longest_prime_len = 0

    while y + len(seq) < len(all_primes) and total < UPPER_LIMIT:
        #print "total is...{}".format(total)
        if is_prime(total, all_primes):
            longest_prime_len = len(seq)
            #print 'new prime seq! {}'.format(longest_prime_len)
            #print 'and the total is...{}'.format(total)

        seq.append(all_primes[y+len(seq)])
        total = sum(seq)

    return longest_prime_len

longest_len = 0
originator = 0
for p in xrange(len(all_primes)):
    tmp_len = longest_seq(p)
    if tmp_len > longest_len:
        longest_len = tmp_len
        originator = p

print originator, longest_len
print sum(all_primes[originator:originator+longest_len])

