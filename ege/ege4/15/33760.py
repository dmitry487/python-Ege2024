def del_(n, m):
    return n%m == 0


for a in range (1, 500):
    flag = True

    for x in range (1, 500):
        if not(
            (del_(120, a)) and (del_(x, 36)) <= ((not(del_(x, a))) <= (not(del_(x, 45))))
        ):flag = False

    if flag:
        print(a)