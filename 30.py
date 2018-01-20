# Max is 6 digits, because the maximum sum for 7 digits is 7*(9**5) < 10*6

pows = [x**5 for x in range(10)]
ans = []
for num in xrange(10**6):
    num_sum = sum([pows[int(char)] for char in str(num)])
    if num%(10**4)==0:
        print num
    if num_sum == num:
        ans.append(num)

print ans
