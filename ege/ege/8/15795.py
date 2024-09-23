kolichestvo = 0

for a1 in ('прус'):
    for a2 in ('прус'):
        for a3 in ('прус'):
            for a4 in ('прус'):
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                print(kolichestvo, word)
                break