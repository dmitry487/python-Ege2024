for n in range (1, 10000):
    n_bin = bin(n)[2:]
    n_bin = n_bin.replace('1', '3')
    n_bin = n_bin.replace('0', '1')
    n_bin = n_bin.replace('3', '0')
    n_bin.strip('0')
    r = int(n_bin, 2)
    if (n - r) == 979:
        print(n)
        break