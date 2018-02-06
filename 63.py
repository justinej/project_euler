# Find the number of n-digit positive integers

def n_digits_exponents(digit):
    power = 1
    product = digit**power
    while len(str(product)) == power:
        power += 1
        product = product * digit
    return power-1

ans = 0
for digit in xrange(1,10):
    max_power = n_digits_exponents(digit)
    ans += max_power
print "ans is {}".format(ans)

