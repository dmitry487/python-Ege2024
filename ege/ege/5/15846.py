for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if n%2 == 0:
        n_bin += '00'
    else:
        n_bin += '11'
    r = int(n_bin, 2)
    if r > 115:
        print(n)
        break