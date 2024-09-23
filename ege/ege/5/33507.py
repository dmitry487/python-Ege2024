for n in range(4, 100):
    n_bin = bin(n)[2:]
    n_bin = str(n_bin)
    n_bin =n_bin[:-1] + n_bin[1] + n_bin [1]    
    r = int(n_bin, 2)
    if r > 92:
        print(n)
        break
    
   


