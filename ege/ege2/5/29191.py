for n in range (1, 1000):
    n_bin = bin(n)[2:]
    first = n_bin[:1]
    vtor_bin = n_bin[1:]
    second = vtor_bin[:1]
    n_bin = n_bin + second + first
    r = int(n_bin, 2)
    if r > 74:
        print(n)
        break
