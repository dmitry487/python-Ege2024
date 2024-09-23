kolichestvo = 0
for a1 in 'мнгуст':
    for a2 in 'мангуст':
        for a3 in 'мангуст':
            for a4 in 'мангуст':
                for a5 in 'мангуст':
                    for a6 in 'мангуст':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if word.count('у') > 0 and word.count('м') == 2:
                            kolichestvo += 1
    
print(kolichestvo)