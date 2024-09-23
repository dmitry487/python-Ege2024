kolichestvo = 0
for a1 in 'влту':
    for a2 in 'влту':
        for a3 in 'влту':
            for a4 in 'влту':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if kolichestvo == 98:
                    print(word, kolichestvo)