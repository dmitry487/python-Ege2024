print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if ((x and w) or (w and z)) == ((z <= y) and (y <= x)):
                    print(x,y,z,w)

#yzwx - otvet