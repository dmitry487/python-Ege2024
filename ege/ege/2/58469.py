print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if (x or  (not(y))) <= (w == z) and\
                not((x or (not(y))) == (w <= z)):
                    print(w, x, y, z)

#ywxz - otevet 