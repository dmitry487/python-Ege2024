kolichestvo = 0
for a1 in ('никола'):
    for a2 in ('николай'):
        for a3 in ('николай'):
            for a4 in ('николай'):
                word = a1 + a2 + a3 + a4
                if word.count('и') > 0 or word.count('о') > 0 or\
                word.count('а'):
                    kolichestvo += 1

print(kolichestvo)