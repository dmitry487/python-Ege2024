for n in range(2, 1000):
    n_bin = bin(n)[2:]
    
    n_bin += n_bin[1] + n_bin[0]

    r = int(n_bin, 2)

    if r > 74:
        print(n)
        break
    



