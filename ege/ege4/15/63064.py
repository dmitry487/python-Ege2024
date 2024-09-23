for a in range (500):
    flag = True

    for x in range (500):
        if not(
            ((x&45 > 0) or (x&89 > 0)) <= (x&a > 0)
        ):flag = False

    if flag:
        print(a)
        break