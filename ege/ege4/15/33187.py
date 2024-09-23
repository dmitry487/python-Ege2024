def del_(n, m):
    return n%m == 0


for a in range (1, 400):
    flag = True

    for x in range (1, 400):
        if not(
            (del_(90, a)) and ((not(del_(x, a))) <= ((del_(x, 15)) <= (not(del_(x, 20)))))
        ):flag = False


    if flag:
        print(a)
