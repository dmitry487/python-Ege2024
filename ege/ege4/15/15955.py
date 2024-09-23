for a in range (1, 600):
    flag = True

    for x in range (1, 600):
        for y in range (1, 600):
            if not(
                ((a(x)) <= (x ** 2 <= 81)) and ((y ** 2 <= 36) <= (a(y)))
            ):flag = False

    if flag:
        print(a)
        break