from itertools import *
def f(x, y, z, w):
    return ((x and w) or (w and z)) == ((z <= y) and (y <= x))


for a in product([0, 1], repeat=2): 
    t = [
        (1, 0, 1, 1),
        (1, 0, a[0], 0),
        (1, 0, a[1], 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))
