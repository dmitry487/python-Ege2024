kolichestvo = 0
for a1 in 'лнрт':
    for a2 in 'лнрт':
        for a3 in 'лнрт':
            for a4 in 'лнрт':
                for a5 in 'лнрт':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1

                    if kolichestvo == 150:
                        print(word, kolichestvo)