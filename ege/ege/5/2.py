for n in range (1000, 1, -1):
    n_bin = bin(n)[2:]
    if n % 3 == 0:
        n_bin = n_bin.replace('0', '11')
    if n % 3 != 0:
        n_bin = n_bin.replace('1', '10')
    r = int(n_bin, 2)
    if r <= 161:
        print(r, n)
        