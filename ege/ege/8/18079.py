kolichestvo = 0
for a1 in 'кот':
    for a2 in 'кот':
        for a3 in 'кот':
            for a4 in 'кот':
                for a5 in 'кот':
                    for a6 in 'кот':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('к') == 1:
                            kolichestvo += 1

print(kolichestvo)