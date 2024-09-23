for n in range (9999, 1000, -1):
    n_bin = bin(n)[2:]
    n_bin = str(n_bin)
    c = n_bin[0] + n_bin[1]
    b = n_bin[1] + n_bin[2]
    d = n_bin[2] + n_bin[3]
    first = max(c, b, d)
    print(str(first))
    second = str(c + b + d) - (str(max(c, b, d)) + str(min(c, b, d)))
    n_bin1 = first + second
    r = int(n_bin1, 2)
    if r == 1517:
        print(r)