kolichestvo = 0

for a1 in 'мстф':
    for a2 in 'мстф':
        for a3 in 'мстф':
            for a4 in 'мстф':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1


                if kolichestvo == 138:
                    print(word)