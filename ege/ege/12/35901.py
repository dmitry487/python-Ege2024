for s in range (1, 10000):
    s = str(s)
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
        if s == (50 * '1' + 12 * '2' + 7 * '3'):
            print(s)
