kolichestvo = 0
for a1 in 'конфета':
    for a2 in 'конфета':
        for a3 in 'конфета':
            for a4 in 'конфета':
                for a5 in 'конфета':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('е') == 2 and a2 != 'ф':
                        kolichestvo += 1

print(kolichestvo)