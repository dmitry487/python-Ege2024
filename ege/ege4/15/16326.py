def del_(n, m):
    return n%m == 0


for a in range (1, 500):
    flag = True


    for x in range (1, 500):
        if not(
            (not(del_(x, a))) <= (((del_(x, 14)) <= (not(del_(x, 4)))))
        ):flag= False


    if flag:
        print(a)
        