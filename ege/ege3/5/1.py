for n in range (1, 1000):
    n_bin = bin(n)[2:]

    if n_bin.count('1')%2 == 0:
        n_bin += '0'
        n_bin = n_bin[2:]
        n_bin = '10' + n_bin
    else:
        n_bin += '1'
        n_bin = n_bin[2:]
        n_bin = '11' + n_bin

    r = int(n_bin, 2)
    if r < 35:
        print(n)