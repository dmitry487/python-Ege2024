print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if ((x <= y) or (y == w)) and ((x or z) == w):
                    print(x, y, z, w)

#zyxw - otvet