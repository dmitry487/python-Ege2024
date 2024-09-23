kolichestvo = 0
for a1 in 'abcx':
    for a2 in 'abcx':
        for a3 in 'abcx':
            for a4 in 'abcx':
                for a5 in 'abcx':
                    word = a1 + a2 + a3 + a4 + a5
                    if (word.count('x') == 1 and a1 == 'x') or\
                    (word.count('x')) == 0:
                        kolichestvo += 1


print(kolichestvo)
            