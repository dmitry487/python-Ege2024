for a in range (500):
    flag = True


    for x in range (500):
        for y in range (500):
            if not(
                ((x + 2 * y) < a) or (y > x) or (x > 60)
            ):flag = False


    if flag:
        print(a)
        break