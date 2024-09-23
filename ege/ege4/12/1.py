for n in range (3, 1000):
    s= '3' + n * '5'

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)