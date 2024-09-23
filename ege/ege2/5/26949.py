for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if n_bin.count('1')%2 == 0:
        n_bin += '00'
    else:
        n_bin += '11'

    r = int(n_bin, 2)
    if r <94:
        print(n)
        