for a in range (200):
    flag = True

    for x in range (200):
        for y in range (200):
            if not(
                ((2 * x + 3 * y) < a) or (x >= y) or (y > 24)
            ):flag = False
    if flag:
        print(a)
        break