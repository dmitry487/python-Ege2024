for n in range (1, 1000):
    n_bin = bin(n)[2:]
    n_bin += bin(n%2)[2:]
    n_bin += bin(n%2)[2:]
    r = int(n_bin, 2)
    if r > 123:
        print(r)
        break
