print('x y z')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            if not((x == z) or (x <= (y and z))):
                print(x, y, z)


#yzx - otvet