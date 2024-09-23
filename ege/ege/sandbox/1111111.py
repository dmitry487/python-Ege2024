bad_combos = []

for i in 'aassdd':
        for j in 'aassdd':
            bad_combos.append(i)
            print(bad_combos)


kolichestvo = 0
for a1 in 'asd':
    for a2 in 'asd':
        for a3 in 'asd':
            for a4 in 'asd':
                for a5 in 'asd':
                    for a6 in 'asd':
                        for a7 in 'asd':
                            word = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            if bad_combos not in word:
                                kolichestvo += 1
                                print(kolichestvo, word)
