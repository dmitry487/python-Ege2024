for a in range (400):
    flag = True

    for x in range (400):
        for y in range (400):
            if not(
                (x + 2 * y < a) or\
                (y > x) or (x > 20)
            ): flag = False
        
    if flag:
        print(a)
        break