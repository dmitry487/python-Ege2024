kolichestvo = 0
for a1 in ('бкфц'):
    for a2 in ('бкфц'):
        for a3 in ('бкфц'):
            for a4 in ('бкфц'):
                for a5 in ('бкфц'):
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1

                    if kolichestvo == 239:
                        print(word, kolichestvo)
