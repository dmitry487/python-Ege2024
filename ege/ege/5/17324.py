kolichestvo = 0
for n in range (10, 1000):
    n_bin = bin(n)[3:]
    n_bin = bin(int(n_bin, 2))[2:]
    res = int(n_bin, 2)
    otvet = res - n
    print((otvet))



    