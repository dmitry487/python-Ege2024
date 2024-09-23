kolichestvo = 0
for a1 in 'метро':
    for a2 in 'метро':
        for a3 in 'метро':
            for a4 in 'метро':
                word = a1 + a2 + a3 + a4
                if (a1 == 'м' or a1 == 'т' or a1 == 'р') and\
                ((a4 == 'е') or (a4 == 'о')):
                    kolichestvo += 1

print(kolichestvo)