for n in range (10000, 1000, -1):
    n_bin = str(n)
    first = int(n_bin[0]) + int(n_bin[1])
    second = int(n_bin[1]) + int(n_bin[2])
    third = int(n_bin[2]) + int(n_bin[3])
    naib = str(max(first, second, third))
    sr = str(first + second + third - max(first, second, third) - min(first, second, third))
    res = naib + sr
    if res == '1515':
        print(n)
        break