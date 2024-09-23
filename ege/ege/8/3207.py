kolichestvo = 0 
for a1 in 'кор':
    for a2 in 'кор':
        for a3 in 'кор':
            for a4 in 'кор':
                for a5 in 'кор':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1
                    if kolichestvo == 238:
                        print(word, kolichestvo)