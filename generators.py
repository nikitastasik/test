from random import *

def randoms(min, max, n):
    for i in range(n):
        yield randint(min, max)

from itertools import *

rand_seq = randoms(1, 10, 10)

five_taken = list(islice(rand_seq, 5))

print(five_taken )