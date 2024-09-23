for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if n_bin.count('1')%2 == 0:
        n_bin = '10' + n_bin[2:] + '0'
    else:
        n_bin = '11' + n_bin[2:] + '1'

    r = int(n_bin, 2)
    if r > 40:
        print(n)
        break