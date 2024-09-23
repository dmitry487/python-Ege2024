kolichestvo = 0
for a1 in 'амух':
    for a2 in 'амух':
        for a3 in 'амух':
            for a4 in 'амух':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if word == 'хухх':
                    print(kolichestvo, word)
                    