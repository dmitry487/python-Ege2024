for a in range (500):
    flag = True

    for x in range (500):
        for y in range (500):
            if not(
                (x < a) or (y < a) or (y > (x - 5)) or (y < (2 * x - 15))
            ):flag = False


    if flag:
        print(a)
        break