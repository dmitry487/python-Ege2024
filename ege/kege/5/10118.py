def to3(num):
    res = ''
    while num > 0:
        res += str(num%3)
        num //= 3
    return res[::-1]



for n in range(1, 10**4):
    n_3 = to3(n)

    if n%4 == 0:
        n_3 = n_3[-3:] + n_3
    else:
        n_3 += to3(n%4*4)

    r = int(n_3, 3)

    if r < 127:
        print(n)
        