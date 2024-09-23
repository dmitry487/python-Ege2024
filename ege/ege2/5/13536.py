kolichestvo = 0
for n in range (1000, 10000):
    n_str = str(n)
    first = int(n_str[0]) + int(n_str[1])
    second = int(n_str[2]) + int(n_str[3])
    max_ = max(first, second)
    min_ = min(first, second)
    res = str(min_) + str(max_)
    if res == '414':
        kolichestvo += 1


print(kolichestvo)