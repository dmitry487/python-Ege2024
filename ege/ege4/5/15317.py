for n in range (10 ** 6):
    n_bin = bin(n)[2:]


    if n%2 == 0:
        n_bin += '01'

    else:
        n_bin = '1' + n_bin + '1'


    r = int(n_bin, 2)


    if r > 156:
        print(n)
        break