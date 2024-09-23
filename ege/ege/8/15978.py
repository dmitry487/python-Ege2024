kolichestvo = 0
for a1 in 'клнтэ':
    for a2 in 'клнтэ':
        for a3 in 'клнтэ':
            for a4 in 'клнтэ':
                for a5 in 'клнтэ':
                    for a6 in 'клнтэ':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        kolichestvo += 1
                        if word == 'кклклк':
                            print(word, kolichestvo)