kolichestvo = 0



for a1 in 'аезикортэ':
    for a2 in 'аезикортэ':
        for a3 in 'аезикортэ':
            for a4 in 'аезикортэ':
                for a5 in 'аезикортэ':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1


                    if ((a1 != 'т') and (word.count('а') <= 2) and
                    (1 <= word.count('з') <= 2)):
                        print(word, kolichestvo)