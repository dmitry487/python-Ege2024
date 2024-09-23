for n in range (10**6):
    n_bin = bin(n)[2:]


    if n_bin.count('1')%2 == 0:
        n_bin += '1'

    else:
        n_bin += '0'


    if n_bin.count('1')%2 == 0:
        n_bin += '1'

    else:
        n_bin += '0'

    r = int(n_bin, 2)

    if r > 54:
        print(r)
        break
