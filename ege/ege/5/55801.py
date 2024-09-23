for n in range (1, 10000):
    n_bin = bin(n)[2:]
    if n%3 == 0:
        n_bin += n_bin[-3]
    else:
        n_bin += bin