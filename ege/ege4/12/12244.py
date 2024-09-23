for n in range (3, 10001):
    s = '3' + n * '5'


    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s= s.replace('333', '5', 1)


    for i in range (20, 1, -1):
        if '5' * i in s:
            print(s)
            break