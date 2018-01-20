# Permuted multiples

def digits(x):
    x = str(x)
    digits = dict([(str(d), 0) for d in xrange(10)])
    for char in x:
        digits[char] = digits[char] + 1
    return digits

def check_anagrams(x):
    for y in xrange(1, 7):
        if not digits(x) == digits(y*x):
            return False
    return True

def find_permuted_multiples():
    length = 2
    while True:
        lower_limit = 10**(length-1)
        upper_limit = 10**length / 6
        
        for candidate in xrange(lower_limit, upper_limit + 1):
            if check_anagrams(candidate):
                return candidate
        length += 1
        print "onto new length: {}".format(length)

print(find_permuted_multiples())
