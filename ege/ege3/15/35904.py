def del_(n, m):
    return n%m == 0


for a in range (1, 3000):
    flag = True


    for x in range (1, 3000):
        if not(
            (del_(a, 40)) and ((del_(780,x)) <= ((not(del_(a, x))) <= (not(del_(180, x)))))
        ):flag = False


    if flag:
        print(a)
        break