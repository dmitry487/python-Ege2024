for a in range (1, 100):
    flag = True


    for x in range(1, 100):
        if not(
            ((x&29) != 0) <=\
            (((x&17) == 17) <= ((x&a) !=0))
        ): flag = False

    if flag:
        print(a)
        break