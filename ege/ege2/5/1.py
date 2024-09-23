kolichestvo = 0
for n in range (10**7):
    n_bin = bin(n)[2:]
    n_bin += bin(n%4)[2:]
    r = int(n_bin, 2)
    if r in range (1000000000, 1789456123):
        kolichestvo += 1

print(kolichestvo)
