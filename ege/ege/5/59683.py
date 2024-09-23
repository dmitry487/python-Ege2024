for n in range (1000, 1, -1):
    n_bin = bin(n)[2:]
    if n % 3 == 0:
        n_bin += (bin(n%3)[2:])
    else:
        n_bin += (bin(n%3)[2:])
    r = int(n_bin, 2)
    if r <= 170:
        print(r)
        break
