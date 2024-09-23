def del_(n, m):
    return n%m == 0

for a in range (1, 500):
    flag = True


    for x in range (1, 500):
        if not(
            (not(del_(x, a))) <= ((del_(x, 28)) <= (not(del_(x, 49))))
        ):flag = False


    if flag:
        print(a)
        