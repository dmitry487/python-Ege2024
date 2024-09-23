kolichestvo = 0
for a1 in 'абвгд':
    for a2 in 'абвгд':
        for a3 in 'абвгд':
            for a4 in 'абвгд':
                for a5 in 'абвгд':
                    word = a1 + a2 + a3 + a4 + a5
                    if (a1 != 'а') and ('аа' not in word) and ('бб' not in word) and\
                    ('вв' not in word) and ('гг' not in word) and ('дд' not in word):
                        kolichestvo += 1

print(kolichestvo)