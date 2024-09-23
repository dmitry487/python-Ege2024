kolichestvo = 0

for a1 in 'виктор':
    for a2 in 'виктор':
        for a3 in 'виктор':
            for a4 in 'виктор':
                for a5 in 'виктор':
                    for a6 in 'виктор':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        kolichestvo += 1

                        if kolichestvo == 170:
                            print(word, kolichestvo)
                    