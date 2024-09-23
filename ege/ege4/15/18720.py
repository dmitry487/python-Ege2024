for a in range (500):
    flag = True


    for x in range (500):
        for y in range (500):
            if not(
                (x * y < a) or (x < y) or (x >= 12)
            ):flag = False

    if flag:
        print(a)
        break