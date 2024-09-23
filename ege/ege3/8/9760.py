kolichestvo = 0


for a1 in 'ABCX':
    for a2 in 'ABCX':
        for a3 in 'ABCX':
            for a4 in 'ABCX':
                for a5 in 'ABCX':
                    word = a1 + a2 + a3 + a4 + a5
                    if ((word.count('X') == 0) or ((a1 == 'X') and word.count('X') == 1)):
                        kolichestvo += 1


print(kolichestvo)