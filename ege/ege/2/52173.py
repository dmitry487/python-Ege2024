print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not((z == (not(x))) <= ((w <= (not(y))) and (y <= x))):
                    print(x,y,z,w)

#yzxw - otvet