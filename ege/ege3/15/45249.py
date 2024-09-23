def del_(n, m):
    return n%m == 0


for a in range (300):
    flag = True


    for x in range (300):
        if not(
            ((del_(x, 3)) <= (not(del_(x, 5)))) or (x + a >= 90)
        ): flag = False


    if  flag:
        print(a)
        break