# Find smallest cube where 5 permutations are also cubes

def positions(digits):
    all_permutations = []
    queue = [[x] for x in xrange(digits)]
    while len(queue) > 0:
        sub_pos = queue.pop()
        if len(sub_pos) == digits:
            all_permutations.append(sub_pos)
        else:
            options = [x for x in range(digits) if x not in sub_pos]
            for option in options:
                queue.append(sub_pos + [option])
    return all_permutations

def permute(x, pos):
    x = str(x)
    y = ''
    for spot in pos:
        y = y + x[spot]
    return int(y)

def permutations(x, positions):
    ans = []
    for pos in positions:
        ans.append(permute(x, pos))
    return list(set(ans))

def ceil(x):
    if x == int(x):
        return int(x)
    else: return int(x)+1

def all_cubes(lower, upper):
    ans = []
    for i in xrange(lower, upper):
        ans.append(i**3)
    return ans

def group_cubes(cubes):
    ans = {}
    for cube in cubes:
        sort_cube = int("".join(sorted([char for char in str(cube)])))
        if sort_cube in ans: ans[sort_cube].append(cube)
        else: ans[sort_cube] = [cube]
    return ans

def find_cube(num):
    num_digits = 9 # Num digits in cube
    flag = True
    while flag:
        cubes = all_cubes(ceil(10**((num_digits-1)/3.)), ceil(10**(num_digits/3.)))
        families = group_cubes(cubes)
        print "There are approx {} cubes with {} digits".format(len(cubes), num_digits)
        for sort_cube in families:
            if len(families[sort_cube]) >= num:
                return families[sort_cube]

        num_digits += 1

print find_cube(5)
