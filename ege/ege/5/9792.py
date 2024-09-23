for n in range (1000, 100, -1):
    n_bin = str(n)
    per = int(n_bin[0]) * int(n_bin[1])
    vtor = int(n_bin[1]) * (n_bin[2])
    if str(per) > str(vtor):
        n_bin = str(vtor) + str(per)
    else:
        n_bin = str(per) + str(vtor)
    if n_bin == '621':
        print(n)
        break
