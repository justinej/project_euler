# Ideas:
# - keep a list of primes (sorted), save it as a file
# - is_prime is a binary search through the list
# - maybe keep it as 2 million primes for now? Can increase later

# Iterate over the sum of primes
# Partition it, see if partition sizes are primes, and then see if
# they combined are primes?
# maybe faster to limit based on which two primes combine to primes..
# So graph? Where edges are based on if they combine to be primes
# Find K5 graph with the smallest total sum... how to do that?

import networkx as nx
import os


###################################################
#Calculates and saves all of the primes up to LIMIT
###################################################
LIMIT = 10**6
filename = "primes.txt"
### Loads list of primes
def load_primes():
    primes = []
    if os.path.exists(filename):
        f = open(filename, "r")
        for line in f:
            primes.append(int(line[:-1]))
        f.close()
    return primes

### Saves list into file
def save_primes(p_sofar, prev_len):
    f = open(filename, "a")
    for prime in p_sofar[prev_len:]:
        f.write(str(prime) + '\n')
    f.close()

def is_prime(x, primes):
    if x in primes:
        return True
    for p in primes:
        if x%p==0:
            return False
    return True

### Finds all primes under x
def all_primes(x):
    p_sofar = load_primes()
    prev_len = len(p_sofar)
    if prev_len == 0:
        start = 2
    else: start = p_sofar[-1]+1

    for i in xrange(start, x):
        if is_prime(i, p_sofar):
            p_sofar.append(i)
        if i%10**4 == 0:
            print "Calculating primes step {} out of {}".format(i, x)
    save_primes(p_sofar, prev_len)
    return p_sofar

primes = all_primes(LIMIT)


################################################
# Creates a graph with the primes
################################################

G = nx.Graph()
for p in primes:
    G.add_node(p)

prime_set = set(primes)
print "Adding edges to graph"
for i in xrange(len(primes)):
    if i%10**3 == 0:
        print "Adding edge {} out of {}".format(i, len(primes))
    for j in xrange(i, len(primes)):
        if int(str(primes[i]) + str(primes[j])) in prime_set and int(str(primes[j]) + str(primes[i])) in prime_set:
            G.add_edge(primes[i], primes[j])

print "Finding max cliques"
max_len = 0
max_graphs = []
for subgraph in nx.find_cliques(G):
    if len(subgraph) > max_len:
        max_graphs = [subgraph]
        max_len = len(subgraph)
    elif len(subgraph) == max_len:
        max_graphs.append(subgraph)
print max_graphs
