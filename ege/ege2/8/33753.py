kolichestvo = 0
for a1 in 'андрей':
    for a2 in 'андрей':
        for a3 in 'андрей':
            for a4 in 'андрей':
                for a5 in 'андрей':
                    for a6 in 'андрей':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('а') > 0 and word.count('й') < 2:
                            kolichestvo += 1

print(kolichestvo)