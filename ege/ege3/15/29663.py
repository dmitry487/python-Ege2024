def del_(n, m):
    return n%m == 0



for a in range (1, 300):
    flag = True


    for x in range (1, 300):
        if not(
            (a < 50) and (((not(del_(x, a)))) <= ((del_(x, 10)) <= (not(del_(x, 12)))))
        ):flag = False


    if flag:
        print(a)