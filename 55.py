# Find all Lychrel numbers below 10,000

def reverse(x):
    return int(str(x)[::-1])

def iterate(x):
    return x + reverse(x)

def find_lychrel_numbers(limit):
    lychrel_nums = []
    for x in xrange(limit):
        i = 1
        x = iterate(x)
        while x != reverse(x) and i < 50:
            i += 1
            x = iterate(x)
        if x != reverse(x):
            lychrel_nums.append(x)
    return len(lychrel_nums)
            

limit = 10**4
print find_lychrel_numbers(limit)

