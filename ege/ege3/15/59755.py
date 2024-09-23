for a in range (2000):
    flag = True


    for x in range (2000):
        for y in range (2000):
            if not((x < a) or (y > a) or (y < x - 1) or (y < 2 * x - 3)):
                flag = False


    if flag:
        print(a)
        break