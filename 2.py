i = 1 # index of the term
total = 0
f_j = 1 # Where j is implied to be i-1
f_i = 1

while f_i <= 4*(10**6):
    if f_i % 2 == 0:
        total += f_i
    i += 1
    f_j_tmp = f_j
    f_j = f_i
    f_i = f_i + f_j_tmp

print total
