def del_(n, m):
    return n%m == 0



for a in range (1, 300):
    flag= True


    for x in range (1, 300):
        if not(
            (del_(a, 45)) and ((del_(750, x) <= ((not(del_(a, x))) <= (not(del_(120, x))))))
        ):flag= False



    if flag:
        print(a)
        break