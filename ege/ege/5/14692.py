for n in range (10000, 1000, -1):
    n_bin = str(n)
    first = int(n_bin[0] + n_bin[1])
    second = int(n_bin[1] + n_bin[2])
    third = int(n_bin[2] + n_bin[3])
    max_ = max(first, second, third)
    min_ = min(first, second, third)
    sr = (int(first + second + third) - max(first, second, third) -  min(first, second, third))
    res = str(sr) + str(max_)
    if res == '613':
        print(res)
