for a in range (500):
    flag = True


    for x in range (500):
        if not(
            ((x&20777) != 0) <= (((x&12332) == 0) <= ((x&a) !=0))
        ):flag = False


    if flag:
        print(a)
        break