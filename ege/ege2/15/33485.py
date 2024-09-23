def del_(n, m):
    return n%m == 0

for a in range (1, 300):
    flag = True


    for x in range (1, 300):
        if not(
            del_(120, a) and ((not(del_(x, a))) <= ((del_(x, 18)) <= (not(del_(x, 24)))))
        ):
            flag = False

    if flag:
        print(a)