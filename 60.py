# TIME COMPLEXITY IS REAL!!! This sieve thing is so powerful
# Okay but you gotta do incremental sieve or else it's gonna flood yo memory
# Answer: sum([13, 5197, 5701, 6733, 8389]) = 26033
# Dunno why it takes a while (where a while is like...<5 minutes)

def calculate_primes(limit):
    nums = [True for x in xrange(limit)]
    nums[0] = False
    nums[1] = False

    for i in xrange(2, int(limit**0.5)):
        if nums[i]:
            for j in [i*(i+k) for k in range( int((float(limit-1)/i) - i) + 1)]:
                nums[j] = False
    return [p for p in xrange(limit) if nums[p]]

def ceil(x):
    if int(x) == x:
        return int(x)
    else: return int(x)+1

def multiples_in_range(p, lower, upper):
    lowest_multiplier = ceil(lower/float(p))
    highest_multiplier = ceil(upper/float(p))
    return [p*x for x in xrange(lowest_multiplier, highest_multiplier)]

def binary_search(x, values):
    # Assumes values is sorted in increasing order
    # Returns index of least value > x
    lower, upper = 0, len(values)-1
    tmp = values[(lower+upper)/2]
    while tmp != x and upper-lower>1:
        if tmp > x: upper = (lower+upper)/2
        else: lower = (lower+upper)/2
        tmp = values[(lower+upper)/2]

    if upper-lower == 1:
        if values[upper] < x: return upper + 1
        elif values[lower] < x: return upper
        else: return lower

    if tmp == x:
        return (lower+upper)/2 + 1
    
def segmented_sieve(limit):
    delta = int(limit**0.5)
    primes = calculate_primes(delta)
    for i in xrange(1, limit/delta+1):

        if i%100 == 0:
            print "done with {} out of {} for segmented sieve".format(i, limit/delta+1)
        # Represents [i*delta, i*delta+1, ... (i+1)*delta-1]
        nums = [True for x in xrange(delta)]
        m = (i+1)*delta - 1
        primes_to_check = primes[:binary_search(int(m**0.5), primes)]
        #primes_to_check = [p for p in primes if p <= m**0.5]

        for p in primes_to_check:
            for multiple in multiples_in_range(p, i*delta, (i+1)*delta):
                nums[multiple - i*delta] = False
        primes = primes + [p+i*delta for p in xrange(delta) if nums[p]]
    return primes

def concat(a, b):
    return int(str(a) + str(b))

flag = True
num_digits = 3

while flag:
    all_primes = set(segmented_sieve(10**(2*num_digits)))
    primes = calculate_primes(10**num_digits)
    print("Done calculating primes with {} digits".format(num_digits))

    edges = {}
    for i1 in xrange(len(primes)):
        p1 = primes[i1]
        if i1 == len(primes): continue
        for i2 in xrange(i1+1, len(primes)):
            p2 = primes[i2]
            if concat(p1, p2) in all_primes and concat(p2, p1) in all_primes:
                if p1 in edges:
                    edges[p1].append(p2)
                else: edges[p1] = [p2]
    
    print("Done with edges")
    # key is always smaller than value
    
    edges2 = {}
    for p1 in edges:
        for p2 in edges[p1]:
            if p2 not in edges:
                continue
            p3_list = [p3 for p3 in edges[p2] if p3 in edges[p1]]
            for p3 in p3_list:
                if (p1, p2) in edges2:
                    edges2[(p1, p2)].append(p3)
                else: edges2[(p1, p2)] = [p3]
    print("Done with edges2")
    
    edges3 = {}
    for (p1, p2) in edges2:
        for p3 in edges2[(p1, p2)]:
            if p3 not in edges: continue
            for p4 in edges[p3]:
                if p4 in edges2[(p1, p2)]:
                    if (p1, p2, p3) in edges3:
                        edges3[(p1, p2, p3)].append(p4)
                    else: edges3[(p1, p2, p3)] = [p4]

    print("done with edges3")
    
    k5s = []
    for (p1, p2, p3) in edges3:
        for p4 in edges3[(p1, p2, p3)]:
            if p4 not in edges: continue
            for p5 in edges[p4]:
                if p5 in edges3[(p1, p2, p3)]:
                    k5s.append((p1, p2, p3, p4, p5))
    print("done with k5s")

    if len(k5s) == 0:
        num_digits += 1
    else:
        flag = False
        print len(k5s)
        print min(k5s, key=lambda x: sum(x))

