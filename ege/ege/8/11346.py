kolichestvo = 0
for a1 in 'абвг':
    for a2 in 'абвг':
        for a3 in 'абвг':
            for a4 in 'абвг':
                for a5 in 'абвг':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('а') == 1:
                        kolichestvo += 1

print(kolichestvo)