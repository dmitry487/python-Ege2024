def check(x, y, z, w):
    if (x == 1) and (y == 0): return False
    return True



print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(((x and (not(y))) == (z or (not(w)))) <= (x and z)):
                    if check(x, y, z, w):
                            print(x, y, z, w)

#yzwx - otvet