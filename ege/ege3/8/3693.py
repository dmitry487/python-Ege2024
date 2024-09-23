kolichestvo = 0


for a1 in 'аклош':
    for a2 in 'аклош':
        for a3 in 'аклош':
            for a4 in 'аклош':
                for a5 in 'аклош':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1


                    if word == 'школа':
                        print(kolichestvo)