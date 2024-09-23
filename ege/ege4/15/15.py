for a in range (1000):
    flag = True

    for x in range(1000):
        if not(
            (x&a == 0) or (not((x&37) == 0)) or (not((x&12) == 0))
        ):flag = False

    if flag:
        print(a)
        