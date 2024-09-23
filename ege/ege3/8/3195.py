kolichestvo = 0


for a1 in 'акру':
    for a2 in 'акру':
        for a3 in 'акру':
            for a4 in 'акру':
                for a5 in 'акру':
                    word = a1 + a2 + a3 + a4 + a5   
                    kolichestvo += 1

                    if kolichestvo == 350:
                        print(word)