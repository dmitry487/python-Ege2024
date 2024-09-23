kolichestvo = 0
for a1 in 'винт':
    for a2 in 'винт':
        for a3 in 'винт':
            for a4 in 'винт':
                for a5 in 'винт':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1


                    if kolichestvo == 1020:
                        print(kolichestvo, word)