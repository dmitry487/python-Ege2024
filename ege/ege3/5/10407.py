for n in range(1000, 10000):
    n_str = str(n)

    first = int(n_str[0]) + int(n_str[1])
    second = int(n_str[1]) + int(n_str[2])
    third = int(n_str[2]) + int(n_str[3])

    min_ = min(first, second, third)
    max_ = max(first, second, third)
    sr = (first + second + third) - min_ - max_
    res = str(sr) + str(max_)

    if res == '1515':
        print(n)
        