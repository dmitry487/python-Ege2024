import sys

sys.setrecursionlimit(5000)

for n in range (100, 100000):
    n_bin = str(n)
    first = int(n_bin[0]) * int(n_bin[1])
    second = int(n_bin[1]) * int(n_bin[2])
    print(first,second)
    max_ = max(first,second)
    min_ = min(first, second)
    res = str(min_) + str(max_)
    res = str(res)
    if res == '621':
        print(n)
        break