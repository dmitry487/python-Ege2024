for n in range (1, 10000):
    n_bin = bin(n)[2:]
    print(n_bin)
    n_bin = n_bin[1:]
    if n_bin.count('1')%2 == 0:
        n_bin = n_bin[2:]
    if len(n_bin) == 0:
        res = 0
    else:
        res = int(n_bin, 2)
    