for n in range (128, 255):
    n_bin = bin(n)[2:]
    n_bin = n_bin.replace('0', '2')
    n_bin = n_bin.replace('1', '0')
    n_bin = n_bin.replace('2', '1')
    r = int(n_bin, 2)
    res = n - r
    if res == 105:
        print(n)
