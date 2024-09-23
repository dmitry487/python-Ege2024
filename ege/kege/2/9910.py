from itertools import *
def f(w, x, y, z):
    return ((x <= y) or (z <= w)) and (not(x <= w))


for a in product([0, 1], repeat=5): 
    t = [
        (1, 0, 1, a[0]),
        (1, a[1], a[2], 1),
        (a[3], a[4], 1, 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
                print(''.join(p))









