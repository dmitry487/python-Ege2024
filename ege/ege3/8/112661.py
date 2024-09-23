kolichestvo = 0


for a1 in 'ABCDEX':
    for a2 in 'ABCDEX':
        for a3 in 'ABCDEX':
            for a4 in 'ABCDEX':
                word = a1 + a2 + a3 + a4

                if word.count('X') == 1:
                    kolichestvo += 1



print(kolichestvo)