kolichestvo = 0
for a1 in ('алгоритм'):
    for a2 in  ('алгоритм'):
        for a3 in  ('алгоритм'):
            for a4 in  ('алгоритм'):
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                if a1 == 'г' and a2 == 'о':
                    print(kolichestvo, word)
