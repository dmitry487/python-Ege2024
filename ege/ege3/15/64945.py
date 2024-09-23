for a in range (22000):
    flag = True

    for x in range (22000):
        if not(
            ((x&21074) != 0) <= (((x&12369) == 0) <= ((x&a) != 0))
        ):flag = False

    if flag:
        print(a)
        break

