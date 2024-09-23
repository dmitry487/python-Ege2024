for n in range (1000, 10000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[1]) + int(n_bin[2])
    third = int(n_bin[2]) + int(n_bin[3])
    min_ = min(first, second, third)
    max_ = max(first, second, third)
    sr = (first + second + third) - min_ - max_
    res = str(sr) + str(max_)
    res = str(res)
    if res == '1517':
        print(n)
        break