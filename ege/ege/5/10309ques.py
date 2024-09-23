for n in range (10000, 100000):
    n_bin = bin(n)[2:]
    perv = int(n_bin[0]) + int(n_bin[2]) + int(n_bin[4])
    vtor = int(n_bin[1]) + int(n_bin[3])
    first = str(min(perv, vtor))
    second = str(max(perv, vtor))
    r = first + second
    if r  == '621':
        print(n)
        break

