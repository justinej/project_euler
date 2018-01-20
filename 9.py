# a^2 + b^2 = c^2
# Find a, b, c such that a+b+c=1000

def trips():
    for a in xrange(1000):
        for b in xrange(a):
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                return a, b, c

a, b, c = trips()
print a, b, c
print a*b*c
            
