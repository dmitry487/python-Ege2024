bad_combos = []
chetnie = []

for i in '02468':
    for j in '02468':
        bad_combos.append(i + j)

for i in '1357':
    chetnie.append(i)


def check(num):
    i = 0
    for bad_word in bad_combos:
        for counter in range (1, 8, 2):
            if num.count(str(counter)):
                i += 1
            if (i != 3) and (bad_word in num): return False
            return True

    

kolichestvo = 0
for a1 in '12345678':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                    for a6 in '012345678':
                        for a7 in '012345678':
                            for a8 in '012345678':
                                for a9 in '012345678':
                                    for a10 in '012345678':
                                        for a11 in '012345678':
                                            for a12 in '012345678':
                                                word = a1 + a2 + a3 + a4 + a5 + a5 +\
                                                a6 + a7 + a8 + a9 + a10 + a11 + a12
                                                if check(word):
                                                    kolichestvo += 1


print(kolichestvo)
