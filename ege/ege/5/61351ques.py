kolichestvo = 0
for n in range (1, 1000):
    n_bin = bin(n)[2:]
    ost_ = n_bin.count('1')%3
    ost_ = bin(ost_)[2:]
    n_bin += ost_
    ost_t = n_bin.count('1')%5
    ost_t = bin(ost_t)[2:]
    n_bin += ost_t
    r = int(n_bin, 2)
    if r in range (1111111110,1444444416):
        kolichestvo += 1
print(kolichestvo)

