print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if ((not(x)) or y or z) == ((not(y)) and z and w):
                    print(x, y, z, w)


#ywzx - otvet