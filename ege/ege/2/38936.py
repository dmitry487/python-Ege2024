print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not((x == (not(y))) <= ((x and w) == (z and (not(w))))):
                    print(z, y, z, w)

#wzyx - otvet