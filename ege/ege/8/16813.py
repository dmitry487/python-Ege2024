def f(word):
    if (
        (
            (word.count('л')) == 1 and (word.count('е')) == 1 and\
                  (word.count('в')) == 1 and (word.count('и')) == 1 and\
            (word.count('й')) == 1
        )
    ): return True
    return False

kolichestvo = 0

for a1 in ('леви'):
    for a2 in ('левий'):
        for a3 in ('левий'):
            for a4 in ('левий'):
                for a5 in ('левий'):
                    word = a1 + a2 + a3 + a4 + a5
                    if a1 + a2 != 'еи' and a2 + a3 != 'еи' and a3 + a4 != 'еи' and\
                         a4 + a5 != 'еи' and f(word):
                        kolichestvo += 1
print(kolichestvo)

