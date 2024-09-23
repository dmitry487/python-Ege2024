from string import digits

alph = digits[:9]


for A in range(1, 1000):
    for x in alph:
        M = int('842' + x + '5', 9)
        N = int('8' + x + '725', 9)
        if (M + A) % N == 0:
            print(A)
            break
