for a in range (200):
    flag = True


    for x in range (200):
        for y in range (200):
            if not(
                (3 * x + 4 * y != 60) or ((a >= x) and (a >= y))
            ): flag = False


    if flag:
        print(a)
        break