for n in range (1000, 10000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[2]) + int(n_bin[3])

    min_ = min(first, second)
    max_ = max(first, second)
    res = str(min_) + str(max_)
    if res == '117':
        print(n)
        