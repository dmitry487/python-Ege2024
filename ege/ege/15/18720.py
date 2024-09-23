for a in range (200):
    flag = True

    for x in range (200):
        for y in range (200):
            if not(
                (x * y < a) or\
                (x < y) or (x >= 12)
            ): flag = False

    if flag:
        print(a)
        break
