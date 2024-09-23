from itertools import *

def f(x, y, z, w):
    return (x or y) and (not(y == z)) and (not(w))



for a in product([0, 1], repeat=4): 
    t = [
        (a[0], 1, a[1], 1),
        (0, 0, 1, a[2]),
        (0, a[3], 1, 1),
        ] 
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]: 
                print(''.join(p))