for a in range (400):
    flag = True

    for x in range (400):
        for y in range (400):
            if not(
                (99 != y + 2 * x) or (a < x) or (a < y)
            ):flag = False


    if flag:
        print(a)
