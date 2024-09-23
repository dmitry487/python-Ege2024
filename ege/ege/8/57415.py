kolichestvo = 0
for a1 in 'абзи':
    for a2 in 'абзи':
        for a3 in 'абзи':
            for a4 in 'абзи':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1

                if a1 =='и' and a2 == 'з' and a3 == 'б' and a4 == 'а':
                    print(word, kolichestvo)
