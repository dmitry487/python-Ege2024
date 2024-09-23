print('x y z w')
for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                if not(
                    (not(z) == y) <= ((w and (not(x))) == (y and x))  
                ):print(x, y, z, w)




#zwxy - otvet