for a in range (1000):
    flag = False


    for x in range (1000):
        for y in range (1000):
            if not(
                (5 * x + y > 63) or (x > 2 * y) or (3 * x + 2 * y < a)
            ): flag = True


    if flag:
        print(a)