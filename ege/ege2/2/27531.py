print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if (x <= y) and (y == (not(z))) and (z or w):
                    if w == 1:
                        print(x, y, z, w)


#ywzx - otvet