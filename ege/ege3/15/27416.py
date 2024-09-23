def del_(n, m):
    return n%m == 0


for a in range (1, 300):
    flag = True

    for x in range (1, 300):
        if not(
            (not(del_(x, a))) <= ((del_(x, 6)) <= (not(del_(x, 9))))
        ):flag = False

    if flag:
        print(a)
