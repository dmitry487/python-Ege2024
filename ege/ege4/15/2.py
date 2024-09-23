for a in range (300):
    flag = True

    for x in range (300):
        for y in range (300):
            if (
                ((3 * x + y) > a) and (y < x) and (x < 30)
            ):flag = False



    if flag:
        print(a)
        break