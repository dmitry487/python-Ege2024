kolichestvo = 0
for a1 in 'аиоуэ':
    for a2 in 'аиоуэ':
        for a3 in 'аиоуэ':
            for a4 in 'аиоуэ':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if word == 'иааэ':
                    print(word, kolichestvo)