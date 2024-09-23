kolichestvo = 0
for a1 in 'пир':
    for a2 in 'пир':
        for a3 in 'пир':
            for a4 in 'пир':
                for a5 in 'пир':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('п') == 1:
                        kolichestvo += 1

print(kolichestvo)