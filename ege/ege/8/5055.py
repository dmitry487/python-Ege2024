kolichestvo = 0
for a1 in ('векно'):
    for a2 in ('векно'):
        for a3 in ('векно'):
            for a4 in ('векно'):
                for a5 in ('векно'):
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1

                    if a1 == 'о':
                        print(kolichestvo, word)