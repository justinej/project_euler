def is_palindrome(x):
    for i in xrange( len(str(x)) /2):
        if str(x)[i] != str(x)[ len(str(x)) - 1 - i]:
            return False
    return True

assert(is_palindrome(1))
assert(is_palindrome(122) is False)
assert(is_palindrome(22))
assert(is_palindrome(39293))
assert(is_palindrome(393493) is False)

def max_palindromic_product():
    max_products = [] # max products over a
    for a in xrange(10**3 - 1, 10**2 - 1, -1):
        for b in xrange(10**3 - 1, 10**2 - 1, -1):
            if is_palindrome(a*b):
                max_products.append(a*b)
                break # Move onto next iteraction of a
    return max(max_products)

print(max_palindromic_product()) 
