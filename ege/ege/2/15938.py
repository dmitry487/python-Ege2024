print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not((z and y) or ((x <= z) == (y <= w))):
                    if x == 1:
                        print(x, y, z, w)


#wzyx - otvet