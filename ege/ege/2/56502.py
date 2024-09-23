print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if not(((x <= y) or (z <= w)) and ((z == y) <= (w == x))):
                    if x == 1:
                        print(w,x,y,z)


#yxwz - otvet