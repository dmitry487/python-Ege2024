kolichestvo = 0
for a1 in 'вирт':
    for a2 in 'вирт':
        for a3 in 'вирт':
            for a4 in 'вирт':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if kolichestvo == 249:
                    print(word, kolichestvo)
