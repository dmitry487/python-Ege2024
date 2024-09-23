for a in range (1000):
    flag = True

    for m in range (1000):
        for n in range (1000):
            if not(
                ((2 * m + 3 * n) > 43) or\
                (m < a) or (n <= a)
            ): flag  = False

    if flag:
        print(a)
        break
