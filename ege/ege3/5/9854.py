def to7(num: int):
    digits = ''
    while num > 0:
        digits += str(num%7)
        num //= 7
    return digits[::-1]

for n in range (10 ** 6):
    n_sm = to7(n)
    if ((n_sm.count('1')) + (n_sm.count('2') * 2) + (n_sm.count('3') * 3) +
    (n_sm.count('4') * 4) + (n_sm.count('5') * 5) + (n_sm.count('6') * 6))%2 == 0:
        n_sm += '0'
    else:
        n_sm = n_sm[1:]
        n_sm = '6' + n_sm
    
    r = int(n_sm, 7)

    if r < 119:
        print(r)


