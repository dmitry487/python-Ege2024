print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if not(
                    (not(x <= z)) or (y == w) or y
                ):print(w, x, y, z)


#zxyw - otvet