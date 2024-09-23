for a in range (500):
    flag = True


    for x in range (500):
        for y in range (500):
            if not(
                ((x < a) <= ((x ** 2) < 100)) and (((y ** 2) <= 64) <= (y <= a))
            ):flag = False


    if flag:
        print(a)