kolichestvo = 0

for a1 in 'апрсу':
    for a2 in 'апрсу':
        for a3 in 'апрсу':
            for a4 in 'апрсу':
                for a5 in 'апрсу':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1

                    if word.count('у') <= 1 and 'аа' not in word:
                        print(kolichestvo, word)
                        break