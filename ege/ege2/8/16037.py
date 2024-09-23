kolichestvo = 0

for a1 in 'зима':
    for a2 in 'зима':
        for a3 in 'зима':
            for a4 in 'зима':
                for a5 in 'зима':
                    word = a1 + a2 + a3 + a4 + a5
                    if (word.count('и') == 1 and word.count('а') == 0)\
                        or (word.count('а') == 1 and word.count('и') == 0):
                        kolichestvo += 1

        
print(kolichestvo)