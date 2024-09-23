def to3(num: int):
    digits = ''
    while num > 0:
        digits += str(num%3)
        num //= 3
    return digits[::-1]

for n in range (10 ** 6):
    n_tr = to3(n)
    n_tr += str(n%3)


    r = int(n_tr, 3)
    if r > 1000:
        print(r)
        break