def check(word):
    if (('еа') not in word and ('ае') not in word and ('аи') not in word and\
    ('иа') not in word and ('гр') not in word and ('рг') not in word and\
    ('рс') not in word and ('ср') not in word and ('см') not in word and\
    ('мс') not in word): return False
    if (
        (
            (word.count('г') == 1) and (word.count('е') == 1) and (word.count('р') == 1) and\
            (word.count('а') == 1) and (word.count('с') == 1) and (word.count('и') == 1) and\
            (word.count('м') == 1)
        )
    ):return True
    return False







kolichestvo = 0
for a1 in 'герасим':
    for a2 in 'герасим':
        for a3 in 'герасим':
            for a4 in 'герасим':
                for a5 in 'герасим':
                    for a6 in 'герасим':
                        for a7 in 'герасим':
                            word = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            if check(word):
                                kolichestvo += 1

print(kolichestvo)


    
