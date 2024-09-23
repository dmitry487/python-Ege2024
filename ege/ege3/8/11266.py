kolichestvo = 0


for a1 in 'abcdex':
    for a2 in 'abcdex':
        for a3 in 'abcdex':
            for a4 in 'abcdex':
                word = a1 + a2 + a3 + a4

                if word.count('x') == 1:
                    kolichestvo += 1


print(kolichestvo)