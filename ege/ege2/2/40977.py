print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(((y <= x) and (z or w)) <= ((x and (not(w))) or (y == z))):
                    if z == 1:
                        print(x, y, z, w)


#zwyx - otvet