for a in range (800):
    flag = True

    for x in range (800):
        for y in range (800):
            if not(
                ((y < 20) <= (x > 70)) or (not((x < a) <= (y > a)))
            ):flag = False


    if flag:
        print(a)
        break