from string import digits

alph = digits[:8]

bad_combos = []

for i in '02468':
    for j in '02468':
        bad_combos.append(i + j)


def check(num):
    if (
        (
            (str(num%2)!=0) == 3
        )and
        (
            (num not in bad_combos)
        )
    ):return True
    return False


kolichestvo = 0

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    for a6 in alph:
                        for a7 in alph:
                            for a8 in alph:
                                for a9 in alph:
                                    for a10 in alph:
                                        for a11 in alph:
                                            for a12 in alph:
                                                word = a1 + a2 + a3 + a4 + a5 + a6 +\
                                                a7 + a8 + a9 + a10 + a11 + a12

                                                if check(word):
                                                    kolichestvo += 1
print(kolichestvo)
