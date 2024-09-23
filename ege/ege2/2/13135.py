print('a b c d')
for a in range (0, 2):
    for b in range (0, 2):
        for c in range (0, 2):
            for d in range (0, 2):
                if not(
                    ((not(a)) and (not(b))) or (b == c) or d
                ): print(a, b, c, d)


#cdba - otvet