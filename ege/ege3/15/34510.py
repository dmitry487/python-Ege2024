for a in range (300):
    flag= True

    for x in range(300):
        if not(
            (x&25 != 0) <= ((x&9 == 0) <= (x&a != 0))
        ):flag = False


    if flag:
        print(a)
        break