def del_(m, n):
    return m%n == 0


for a in range (1, 1000):
    flag = True

    for x in range (1, 1000):
        if not(
            ((del_(x, 12)) and ((x&4) == 0)) <= ((x + 1) > a)
        ):flag = False


    if flag:
        print(a)