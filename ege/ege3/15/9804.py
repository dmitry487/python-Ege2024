for a in range (100):
    flag = True

    for x in range(100):
        if not(
            ((x&29) != 0) <= (((x&17) == 0) <= ((x&a) != 0))
        ):flag = False

    if flag:
        print(a)
        break