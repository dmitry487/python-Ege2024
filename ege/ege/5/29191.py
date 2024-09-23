for n in range (1, 10000):
    n_bin = bin(n)[2:]
    n_bin = n_bin + '0' + '1'
    r = int(n_bin, 2)
    if r > 74:
        print(n)
        break