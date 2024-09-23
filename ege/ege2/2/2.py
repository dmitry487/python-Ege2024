from itertools import *
def f(w, x, y, z):
    return ((x == y) <= ((not(z)) or w)) == (not((w <= x) or (y <= z)))


for a in product([0, 1], repeat=5): 
    t = [
        (0, 1, a[0], a[1]),
        (a[2], a[3], 1, 0),
        (0, a[4], 0, 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))
