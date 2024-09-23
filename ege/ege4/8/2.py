alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alph = alph[::-1]
kolichestvo = 0

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    for a6 in alph:
                        for a7 in alph:
                            for a8 in alph:
                                for a9 in alph:
                                    for a10 in alph:
                                        for a11 in alph:
                                            word = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
                                            kolichestvo += 1

                                            if word == 'инорматика':
                                                print(word, kolichestvo)

                            
