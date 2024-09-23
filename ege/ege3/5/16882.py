for n in range(0, 256):
    n_bin = bin(n)[2:]
    n_bin = n_bin.zfill(8)

    n_bin = n_bin.replace('1', '2')
    n_bin = n_bin.replace('0', '1')
    n_bin = n_bin.replace('2', '0')



    r = int(n_bin, 2)

    res = r - n

    if res == 111:
        print(n)