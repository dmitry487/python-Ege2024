for n in range (1, 10000):
    s = ''
    while n > 0:
        s = str(n%3) + s
        s += str(n%3)
        r = int(s, 2)
        if r in range (100, 1000):
            print(r)
            break

    

