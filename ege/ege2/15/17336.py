for a in range (100):
    flag = True
    
    for x in range (100):
        for y in range (100):
            if not(
                (3 * x + 4 * y != 60) or ((a >= x) and (a >= y))
            ):flag = False

    if flag:
        print(a)
        break