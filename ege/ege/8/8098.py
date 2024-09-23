kolichestvo = 0
for a1 in 'слон':
    for a2 in 'слон':
        for a3 in 'слон':
            for a4 in 'слон':
                for a5 in 'слон':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('с') == 1:
                        kolichestvo += 1

print(kolichestvo)
