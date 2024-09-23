from itertools import *

def f(u,w,x,y,z):
    return ((x <= y) and (z == (not(w)))) <= (u == (x or z))



for a in product([0, 1], repeat=8): 
    t = [
        (0, a[0], 0, 0, 0),
        (0, a[1], a[2], 0, 0,),
        (a[3], 0, 0, 0, a[4]),
        (a[5], 0, a[6], a[7], 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('uwxyz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 0]: 
                print(''.join(p))

#wzyxu - otvet