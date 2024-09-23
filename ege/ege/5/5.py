for n in range (1000, 1, -1):
    n_bin = bin(n)[2:]
    ost = int(n_bin)%4
    n_bin = n_bin + str(ost)
    if n_bin[-1] != 3:
        r = int(n_bin, 2)

        if n == 49:
            print(r)
            break