for a in range (100):
    flag = True

    for x in range (100):
        for y in range (100):
            if not(
                (
                    (x + 2 * y < a) or\
                    (y > x) or (x > 60)
                )
            ): flag = False
        
    if flag:
        print(a)
        break