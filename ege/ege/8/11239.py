kolichestvo = 0
for a1 in 'abcdefx':
    for a2 in 'abcdefx':
        for a3 in 'abcdefx':
            for a4 in 'abcdefx':
                word = a1 + a2 + a3 + a4
                if word.count('x') == 1:
                    kolichestvo += 1

print(kolichestvo)