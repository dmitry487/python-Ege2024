print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(((not(z == w)) <= (w and (not(x)))) or (x and (not(y)))):
                    if w == 0:
                        print(x, y, z, w)

#wzyx - otvet