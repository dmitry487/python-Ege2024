for a in range (400):
    flag = True


    for x in range (400):
        for y in range (400):
            if not(
                ((4 * x + 3 * y) < a) or (x > y) or (y > 13)
            ):flag = False

    
    if flag:
        print(a)
        break