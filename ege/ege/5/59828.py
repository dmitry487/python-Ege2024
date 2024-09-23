cifri = []
for n in range(1, 1000):
    n_bin = bin(n)[2:]
    if n%3 == 0:
        n_bin += str(n_bin)[:-3]
    else:
        x = n%3*3
        while x > 0:
            cifri.append(x%3)
            x//=3
        n_bin += str(x)
    r = int(n_bin, 2)
    if r > 150:
        print(n)
        break