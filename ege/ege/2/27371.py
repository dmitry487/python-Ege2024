print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(((x and (not(y))) <= ((not(z)) or (not(w)))) and ((w <= x) or y)):
                    print(x, y, z, w)

#zywx - otvet