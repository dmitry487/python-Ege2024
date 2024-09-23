for n in range (100, 1000):
    n_str = str(n)

    first = int(n_str[0]) * int(n_str[1])
    second = int(n_str[1]) * int(n_str[2])


    min_ = min(first, second)
    max_ = max(first, second)

    res = str(min_) + str(max_)

    if res == '621':
        print(n)