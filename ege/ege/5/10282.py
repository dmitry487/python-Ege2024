for n in range (10000, 100000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[2]) + int(n_bin[4])
    second = int(n_bin[1]) + int(n_bin[3])
    max_ = max(first, second)
    min_ = min(first, second)
    res = str(min_) + str(max_)
    print(res)
    if res == '723':
        print(n)
        break