kolichestvo = 0
for n in range (100, 1000):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[1]) + int(n_bin[2])
    max_ = max(first, second)
    min_ = min(first,second)
    res = str(max_) + str(min_)
    res = str(res)
    if res == '1715':
        kolichestvo += 1

print(kolichestvo)