kolichestvo = 0


for a1 in 'вишня':
    for a2 in 'вишня':
        for a3 in 'вишня':
            for a4 in 'вишня':
                for a5 in 'вишня':
                    for a6 in 'вишня':
                        word = a1 + a2 + a3 + a4 + a5 + a6

                        if ((word.count('в') <= 1) and (a1 == 'ш') and (a6 == 'и' or a6 == 'я')):
                            kolichestvo += 1


                        


print(kolichestvo)