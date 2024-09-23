for n in range(1, 10000):
    n_bin = bin(n)[2:]
    if n_bin.count('1')%2 == 0:
        n_bin = n_bin + '0'
    else:
        n_bin = n_bin + '1'
    if n_bin.count('1')%2 == 0:
        n_bin = n_bin + '0'
    else:
        n_bin = n_bin + '1'
    r = int(n_bin, 2)
    if r > 77:
        print(n)
        break