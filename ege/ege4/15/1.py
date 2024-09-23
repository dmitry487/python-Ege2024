for a in range (500):
    flag = True

    for x in range (500):
        for y in range (500):
            if not(
                (99 != y + 2 * x) or (a < x) or (a < y)
            ):flag = False


    if flag:
        print(a)
        