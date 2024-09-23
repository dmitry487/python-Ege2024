for n in range (100, 1000):
    n_str = str(n)
    first = int(n_str[0]) + int(n_str[1])
    second = int(n_str[1]) + int(n_str[2])
    max_  = max(first, second)
    min_ = min(first, second)
    res = str(max_) + str(min_)
    if res == '159':
        print(n)
        break