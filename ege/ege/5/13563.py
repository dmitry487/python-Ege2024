kolichestvo = 0
for n in range (1000, 10000):
    n_bin = str(n)
    if n%2 == 0:
        first = int(n_bin[0]) + int(n_bin[1])
        second = int(n_bin[2]) + int(n_bin[3])
        min_ = min(first, second)
        max_ = max(first, second)
        res = str(min_) + str(max_)
        res = str(res)
        if res == '616':
            kolichestvo += 1

print(kolichestvo)
