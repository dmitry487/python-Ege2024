for n in range (10 ** 6):
    n_bin = bin(n)[2:]

    if n%3 == 0:
        n_bin += n_bin[-3:]

    else:
        n_bin += bin(n%3)[2:]



    r = int(n_bin, 2)

    if r > 151:
        print(r)
        break