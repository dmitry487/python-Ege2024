from itertools import *

def f(w, x, y, z):
    return ((x or y) <= (y and w)) == (not((y and z) <= (w or x)))



for a in product([0, 1], repeat=2): 
    t = [
        (1, 1, a[0], 1),
        (0, a[1], 0, 0),
        (0, 0, 1, 1),
        ] 
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]: 
                print(''.join(p))