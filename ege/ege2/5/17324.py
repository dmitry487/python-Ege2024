kolichestvo = 0
for n in range (10, 1000):
    n_bin = bin(n)[2:]
    n_bin = n_bin[1:]
    r = int(n_bin, 2)
    n_bin = bin(r)[2:]
    r = int(n_bin, 2)

    res = r - n
    kolichestvo += 1

print(kolichestvo)