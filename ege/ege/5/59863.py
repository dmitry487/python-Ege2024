for n in range (1000, 1, -1):
    n_bin = bin(n)[2:]
    if n%3 == 0:
        n_bin += bin(n)[-3]
        print(n_bin)
    if n%3 != 0:
        n_bin += bin(n%3*3)
    r = int(n_bin, 2)
    if r <= 170:
        print(r)
        break