from itertools import *
def f(x, y, z, w):
    return (not(z == w) <= (w and not(x))) or (x and not(y))



for a in product([0, 1], repeat=6): 
    t = [
        (0, a[0], 0, 0),
        (0, a[1], a[2], 0),
        (0, a[3], a[4], a[5])
        ] 
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))

