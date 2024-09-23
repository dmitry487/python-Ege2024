kolichestvo = 0

for a1 in '123456':
    for a2 in '0123456':
        for a3 in '0123456':
            for a4 in '0123456':
                for a5 in '0123456':
                    for a6 in '0123456':
                        for a7 in '0123456':
                            word = a1 + a2 + a3 + a4 + a5 + a6 + a7

                            chet_count = 0
                            for i in '0246':
                                chet_count += word.count(i)

                            if chet_count == 2:
                                kolichestvo += 1

                            



print(kolichestvo)