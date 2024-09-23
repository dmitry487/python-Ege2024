for n in range (100, 1000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[1]) + int(n_bin[2])
    print(n_bin, first, second)
    min_ = min(first, second)
    max_ = max(first, second)
    res = str(min_) + str(max_)
    if res == '1115':
        print(n)
        break