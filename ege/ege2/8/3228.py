kolichestvo = 0
for a1 in 'аоу':
    for a2 in 'аоу':
        for a3 in 'аоу':
            for a4 in 'аоу':
                for a5 in 'аоу':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1
                    if word == 'уауау':
                        print(word, kolichestvo)