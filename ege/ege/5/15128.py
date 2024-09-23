for n in range (1000, 10000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[1]) + int(n_bin[2])
    third = int(n_bin[2]) + int(n_bin[3])
    max_ = max(first, second, third)
    min_ = min(first, second, third)
    sr = (first + second + third) - max_ - min_
    res = str(sr) + str(max_)
    if res == '1315':
        print(n)