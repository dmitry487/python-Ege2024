for n in range (10 ** 6):
    n_bin = bin(n)[2:]
    n_bin = n_bin.replace('0', '2')
    n_bin = n_bin.replace('1', '0')
    n_bin = n_bin.replace('2', '1')
    r = int(n_bin, 2)
    n_bin = bin(r)[2:]
    r = int(n_bin, 2)
    res = n - r
    if res == 999:
        print(n)
        break