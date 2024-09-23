kolichestvo = 0
for a1 in 'abc':
    for a2 in 'abc':
        for a3 in 'abc':
            for a4 in 'abc':
                for a5 in 'abcx':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('x') == 0 or a5 == 'x':
                        kolichestvo += 1

print(kolichestvo)