def digit(i):
    guess = 1
    i = i-1 # Since 2 diff types of indexing
    while i >= len(str(guess)):
        i -= len(str(guess)) # Move forward that many digits
        guess += 1
    return int(str(guess)[i])

assert(digit(10) == 1)
assert(digit(12) == 1)

ans = 1
for exp in range(7):
    print digit(10**exp)
    ans *= digit(10**exp)
print ans
