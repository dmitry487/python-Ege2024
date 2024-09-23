for n in range (2, 3000):
    n_bin = bin(n)[2:]
    n_bin = n_bin[:-1]
    if n%2 != 0:
        n_bin += '10'
    else:
        n_bin +='01'
    r = int(n_bin, 2)
    if r == 2017:
        print(n)
        
    