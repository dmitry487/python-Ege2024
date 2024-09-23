from string import digits, ascii_lowercase

p = digits + ascii_lowercase


for x in p:
    for y in p:
        res1 = str('12' * '34', p)
        res2 = (x * y**2, p)
        if res1 == res2:
            m = (y * x, p)
            r = int(m, 2)
            print(r)