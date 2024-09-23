kolichestvo = 0


for a1 in 'ольга':
    for a2 in 'ольга':
        for a3 in 'ольга':
            for a4 in 'ольга':
                for a5 in 'ольга':
                    word = a1 + a2 + a3 + a4 + a5
                    if (a1 != 'ь') and ('оь' not in word) and\
                    ('аь' not in word) and (word.count('о') == 1) and\
                        (word.count('л') == 1) and (word.count('ь') == 1) and (word.count('г') == 1) and\
                            (word.count('а') == 1):
                        kolichestvo += 1


print(kolichestvo)
