res = set()

for n in range (100, 3000):
    n_bin = bin(n)[3:]
    if n_bin == '':
        n_bin = '0'
    r = int(n_bin, 2)
    res.add(n - r)

print(len((res)))
    
    