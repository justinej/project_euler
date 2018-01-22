# Maximum digit sum for a**b, a, b < 100

def digit_sum(x):
    ans = 0
    for char in str(x):
        ans += int(char)
    return ans

max_sum = 0
for a in xrange(100):
    for b in xrange(100):
        if digit_sum(a**b) > max_sum:
            max_sum = digit_sum(a**b)
print max_sum
