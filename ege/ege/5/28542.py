for n in range (1000, 10000):
    n_bin = bin(n)[2:]
    n_bin += bin(n%3)[2:]
    r = int(n_bin, 2)
    print(r)
    break
