# Example triangle:
# triangle = [[59],
#     [73, 41],
#     [52, 40, 9],
#     [26, 53, 6, 34],
#     [10, 51, 87, 86, 81]]
#
# Goal: Find maximum total from top to bottom
# Method: Find maximum total for sub-triangles, then add one more layer
# i = current layer
# j = current depth in layer
# max_paths = dictionary with
#   key:i
#   value: list of lists of indexes [ [0, 3, 5, 1] , [...], ... ]
# max_paths[i][j] gives the max path starting at (i, j)


def read_triangle():
    f = open("67-triangle.txt", "r")
    triangle = []
    for line in f:
        row = line[:-1].split(" ")
        row = [int(x) for x in row]
        triangle.append(row)
    return triangle

def path_sum(path, triangle):
    total = 0
    for (i, j) in path:
        total += triangle[i][j]
    return total

triangle = read_triangle()
l = len(triangle)

# Base condition
i = l-2 # Start from second to last row
max_paths = dict( [ [x, []] for x in xrange(l)])
max_paths[i+1] = [ [(l-1, x)] for x in xrange(l)]

# Recursive
while i >= 0:
    for j in xrange(i+1): # i+1 elements in ith row
        assert len(max_paths[i+1]) == i+2
        left_sum = path_sum(max_paths[i+1][j], triangle)
        right_sum = path_sum(max_paths[i+1][j+1], triangle)
        if left_sum > right_sum:
            max_paths[i].append(max_paths[i+1][j] + [(i, j)])
        else: max_paths[i].append(max_paths[i+1][j+1] + [(i, j)])
    i -= 1
print path_sum(max_paths[0][0], triangle)
