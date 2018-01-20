def fds(x):
    fact = 1
    for i in xrange(1, x+1):
        fact *= i
    fact = str(fact)
    ans = 0
    for char in fact:
        ans += int(char)
    return ans

print fds(100)
