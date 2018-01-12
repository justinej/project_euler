total = 0
for x in xrange(101):
    for y in xrange(101):
        if x != y:
            total += x*y

print total
