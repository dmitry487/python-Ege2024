bad_combos = set()

for i in '02468':
    for j in '024680':
        bad_combos.add(i + j)

for i in '13579':
    for j in '13579':
        bad_combos.add(i + j)


def check(word):
    if(
        (
            (word.count('р')) == 1 and (word.count('о')) == 2 and \
            (word.count('с')) == 1 and (word.count('м')) == 1 and \
            (word.count('а')) == 2 and (word.count('х')) == 1
        )
    ):return True
    for i in bad_combos:
        if i in word: return True

    return False

kolichestvo = 0

for a1 in 'росомаха':
    for a2 in 'росомаха':
        for a3 in 'росомаха':
            for a4 in 'росомаха':
                for a5 in 'росомаха':
                    for a6 in 'росомаха':
                        for a7 in 'росомаха':
                            for a8 in 'росомаха':
                                word = a1 + a2 + a3 + a4 + a5 +\
                                a6 + a7 + a8

                                if check(word):
                                    kolichestvo += 1
print(kolichestvo)