kolichestvo = 0
for a1 in ('abcdx'):
    for a2 in ('abcd'):
        for a3 in ('abcd'):
            for a4 in ('abcd'):
                word = a1 + a2 + a3 + a4
                kolichestvo += 1

                print(word, kolichestvo)