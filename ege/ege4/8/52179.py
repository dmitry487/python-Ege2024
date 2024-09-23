kolichestvo = 0
for a1 in 'полина':
    for a2 in 'полина':
        for a3 in 'полина':
            for a4 in 'полина':
                for a5 in 'полина':
                    for a6 in 'полина':
                        for a7 in 'полина':
                            for a8 in 'полина':
                                word = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                                if ((word.count('п') + word.count('л') + word.count('н')) >
                                (word.count('о') + word.count('и') + word.count('а'))):
                                        kolichestvo += 1


print(kolichestvo)

