print('w x y z')
for w in range (0, 2):
    for x in range (0, 2):
        for y in range (0, 2):
            for z in range (0, 2):
                if not(
                    (y and (x or z) or (not(y or z)) or w)
                ):print(w, x, y, z)



#xywz - otvet