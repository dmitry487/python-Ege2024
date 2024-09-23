kolichestvo = 0


for a1 in 'волк':
    for a2 in 'волк':
        for a3 in 'волк':
            for a4 in 'волк':
                for a5 in 'волк':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('в') == 1:
                        kolichestvo += 1


print(kolichestvo)