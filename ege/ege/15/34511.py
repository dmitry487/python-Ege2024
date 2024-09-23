for a in range(1000):
    flag = True

    for x in range(1000):
        if not(
            (x&25 != 0) <=\
            ((x&19 == 0) <= (x&a != 0))
        ): flag = False

    if flag == True:
        print(a)
        break