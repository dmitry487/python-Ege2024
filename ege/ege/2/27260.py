print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(((x or not(y)) and (not(z) == w)) <= (y and z)):
                    print(x, y, z, w)

#yzwx - otvet