for a in range (300):
    flag = True


    for x in range (300):
        for y in range (300):
            if not(
                (y + 2 * x < a) or (x > 30) or (y > 20)
            ): flag = False

    if flag:
        print(a)
        break