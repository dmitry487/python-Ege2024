from itertools import *
def f(w, x, y, z):
    return not((y <= (x == w))) and (z <= x)

for a in product([0, 1], repeat=5): 
    t = [
        (a[0], 1, 1, a[1]),
        (0, a[2], a[3], 0),
        (a[4], 0, 1, 0)
        ] 
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))


print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if not(
                    (y <= (x == w))) and (z <= x):print(w, x, y, z)

#wxyz - otvet   