print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if not((x and y) or (y == z) or w):
                    print(w,x,y,z)
            
#wzyx - otvet