for a in range (300):
    flag = True


    for x in range (300):
        for y in range (300):
            if not(
                (x + 2 * y < a) or\
                (y < x) or (y > 60)
            ): flag = False
    
    if flag:
        print(a)
        break