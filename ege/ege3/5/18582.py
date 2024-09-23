for n in range (10 ** 6):
    n_bin = bin(n)[2:]

    r_pr = int(n_bin, 2)
    n_bin = bin(r_pr)[2:]


    if n_bin.count('1') > n_bin.count('0'):
        n_bin += '1'

    else:
        n_bin += '0'



    r = int(n_bin, 2)

    if r > 100:
        print(r)
        break