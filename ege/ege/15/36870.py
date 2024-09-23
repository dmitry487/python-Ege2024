for a in range (100):
    flag = True

    for x in range (100):
        if not(
            ((x&49) == 0) <=\
            ((x&28 != 0) <=\
            (x&a != 0))
            
        ): flag = False

    if flag:
        print(a)
        break