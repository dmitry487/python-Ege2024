for a in range (100):
    flag = True

    for x in range (100):
        for y in range (100):
            if not(
                (2 * x + 3 * y > 30) or (x + y <= a)
            ):flag = False

    
    if flag:
        print(a)
        break