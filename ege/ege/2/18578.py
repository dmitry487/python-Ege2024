from itertools import *
def f(x, y, z, w):
    return (((x and (not(y))) or (w <= z)) == (z == x))


for a in product([0, 1], repeat=3): 
    t = [
        (a[0], 0, 0, 1),
        (0, 1, 0, 0),
        (0, a[1], a[2], 1)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))