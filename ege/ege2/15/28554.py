for a in range (300):
    flag = True

    for x in range (300):
        for y in range (300):
            if not(
                (x * y < 140) or (y > a) or (x > a)
            ):flag = False

    if flag:
        print(a)
        