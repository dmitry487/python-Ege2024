for a in range (100):
    flag = True

    for x in range (100):
        for y in range (100):
            if not(
                (y  + 2 * x < a) or (x > 15) or (y > 30)
            ):flag = False

    if flag:
        print(a)
        break