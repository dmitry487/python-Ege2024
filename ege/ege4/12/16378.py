for n in range (3, 1001):
    s = '8' + n * '4'

    while '11' in s or '444' in s or '8888' in s:
        s = s.replace('11', '4', 1)
        s = s.replace('444', '88', 1)
        s = s.replace('8888', '1', 1)


    print(s)

    #41