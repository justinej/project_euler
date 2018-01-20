# Combinatoric values > 1 million

chosen = {}
def choose(n, r):
    if (n, r) in chosen:
        return chosen[(n,r)]

    if n == r: ans = 1
    else: # r < n
        ans = choose(n-1, r) * n / (n-r)
    chosen[(n, r)] = ans
    return ans

def num_values():
    ans = 0
    for n in xrange(23, 101):
        for r in xrange(2, n/2):
            if choose(n, r) >= 10**6:
                # print (n,r)
                # print 2*((n/2.)-r) + 1
                ans += 2*((n/2.)-r) + 1
                break
    return ans

print "ans is {}".format(num_values())
