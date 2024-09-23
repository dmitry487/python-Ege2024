for n in range (1, 1000):
    n_bin = bin(n)[2:]
    if str((n.zfil))%2 == 0:
        n_bin += '0'
    else:
        n_bin += '1'
    print(n, n_bin)
