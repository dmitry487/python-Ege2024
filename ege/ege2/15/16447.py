for a in range (500):
    flag = True


    for x in range (500):
        for y in range (500):
            if not(
                (2 * x + 3 * y < 30) or (x + y >= a)
            ):flag = False


    if flag:
        print(a)
