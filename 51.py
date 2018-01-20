def load_primes():
    filename = "primes.txt"
    f = open(filename, "r")
    primes = []
    for line in f:
        primes.append(int(line[:-1]))
    return primes

pos_dict = {}
def get_positions(num_digits, num_slots):
    if (num_digits, num_slots) in pos_dict:
        return pos_dict[(num_digits, num_slots)]

    if num_slots == 1:
        pos_dict[(num_digits, num_slots)] = [[x] for x in range(num_digits)]
    elif num_slots > 1:
        all_pos = []
        smaller_pos = get_positions(num_digits, num_slots-1)
        for pos in smaller_pos:
            for slot in range(pos[-1], num_digits):
                all_pos.append(pos + [slot])
        pos_dict[(num_digits, num_slots)] = all_pos
    else:
        pass
    return pos_dict[(num_digits, num_slots)]

def replace_slots(p, pos, digit):
    for slot in pos:
        p = int(str(p)[:slot] + digit + str(p)[slot+1:])
    return p

family_size = 8
primes = load_primes()

def find_prime(family_size, primes):
    digits = [str(x) for x in xrange(10)]
    prime_set = set(primes)

    for p in primes:
        # First try replacing with one digit
        num_digits = len(str(p))
        positions = get_positions(num_digits, num_digits)
    
        for position in positions:
            results = []
            for digit in digits:
                new_p = replace_slots(p, position, digit)
                if new_p in prime_set and len(str(new_p)) == num_digits:
                    results.append(new_p)
            if len(results) >= family_size:
                print results
                return results[0]

print find_prime(family_size, primes)
