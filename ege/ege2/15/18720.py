for a in range (300):
    flag = True


    for x in range (300):
        for y in range (300):
            if not(
                (x * y < a) or (x < y) or (x >= 12)
            ):flag = False


    if flag:
        print(a)
        break