kolichestvo = 0
for a1 in 'аекр':
    for a2 in 'аекр':
        for a3 in 'аекр':
            for a4 in 'аекр':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1

                if 'а' not in word:
                    print(word, kolichestvo)