spis = []
for n in range (100, 3000):
    n_bin = bin(n)[2:] 
    n_bin = n_bin[1:]
    r = int(n_bin, 2)
    n_bin = bin(r)[2:]
    r = int(n_bin, 2)
    spis.append(n - r)

print(len(set(spis)))
    

