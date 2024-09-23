for n in range (1000000, 1, -1):
    n_bin = bin(n)[2:]
    if n%5 == 0:
        n_bin += bin(5)[2:]
    else:
        n_bin += '1'
    if int(n_bin)%7:
        n_bin = n_bin + bin(7)[2:]
    else:
        n_bin += '1'
    r = int(n_bin, 2)
    if r<1728404:
        print(n)
        break
