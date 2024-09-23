for a in range (1000):
    flag = True


    for x in range (1000):
        if not(
            (x&105 == 0) <=\
            (
                (x&58 != 0) <= (x&a != 0)
            )
        ): flag = False
    
    if flag:
        print(a)
        break