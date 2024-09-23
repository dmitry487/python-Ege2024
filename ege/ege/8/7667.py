kolichestvo = 0
for a1 in (str('ЕЭ')):
    for a2 in (str('ГЕЭ')):
        for a3 in (str('ГЕЭ')):
            for a4 in (str('ГЕЭ')):
                for a5 in (str('ГЕЭ')):
                    word = str(a1 + a2 + a3 + a4 + a5)
                    kolichestvo += 1
                    print(word, kolichestvo)