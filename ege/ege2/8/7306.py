kolichestvo = 0
for a1 in 'ученик':
    for a2 in 'ученик':
        for a3 in 'ученик':
            for a4 in 'ученик':
                for a5 in 'ученик':
                    word = a1 + a2 + a3 + a4 + a5
                    if a1 == 'у' and a2 == 'к':
                        kolichestvo += 1

                    
print(kolichestvo)