kolichestvo = 0
for a1 in ('abx'):
    for a2 in  ('abx'):
        for a3 in  ('abx'):
            for a4 in ('abx'):
                for a5 in ('abx'):
                    for a6 in ('abx'):
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('x') == 1:
                            kolichestvo += 1

                            print(kolichestvo)

