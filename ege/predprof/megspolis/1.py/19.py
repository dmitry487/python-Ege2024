def check(posl):
    if ((posl[0] == (posl[1] * 10)) or (posl[0] == (posl[1]//10))) and\
    (((posl[1] == (posl[2] * 10)) or (posl[1] == (posl[2]//10)))) and\
    ((posl[0] + posl[1] + posl[2]) == 3024):
        return True
    return False
otvet = []
for i in range(1, 1000):
    for j in range (1, 1000):
        for k in range (1, 1000):
            res = []
            res.append(i)
            res.append(j)
            res.append(k)
            if len(res) == 2 and check(res):
                otvet.append(res)


print(otvet)