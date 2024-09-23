for a in range (200):
    flag = True

    for x in range (200):
        for y in range (200):
            if not(
                ((y + 2 * x) != 48) or (a < x) or (a < y)
            ): flag = False

    if flag:
        print(a)