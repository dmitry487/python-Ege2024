kolichestvo = 0
for a1 in 'тимофей':
    for a2 in 'тимофей':
        for a3 in 'тимофей':
            for a4 in 'тимофей':
                for a5 in 'тимофей':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('т') > 0 and word.count('й') <= 1:
                        kolichestvo += 1

print(kolichestvo)