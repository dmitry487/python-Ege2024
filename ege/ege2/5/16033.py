for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if n%2 == 0:
        n_bin += '01'
    else:
        n_bin += '10'

    r = int(n_bin, 2)
    if r > 102:
        print(r)
        break