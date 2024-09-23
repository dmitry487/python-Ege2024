kolichestvo =0
for n in range (10000, 1, -1):
    n_bin = bin(n)[2:]
    ost = n%4
    ost_bin = bin(ost)[2:]
    n_bin += ost_bin
    r = int(n_bin, 2)
    if n == 65:
        kolichestvo += 1
        print(kolichestvo)