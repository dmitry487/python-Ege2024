kolichestvo = 0
for a1 in 'агилморт':
    for a2 in 'агилморт':
        for a3 in 'агилморт':
            for a4 in 'агилморт':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if a1 == 'и' and a2 == 'г':
                    print(word, kolichestvo)