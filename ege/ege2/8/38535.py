kolichestvo = 0


for a1 in 'елмру':
    for a2 in 'елмру':
        for a3 in 'елмру':
            for a4 in 'елмру':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1

                if a1 == 'л':
                    print(kolichestvo)