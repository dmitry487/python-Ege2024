kolichestvo = 0
for a1 in 'апн':
    for a2 in 'апн':
        for a3 in 'апн':
            for a4 in 'апн':
                for a5 in 'апн':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1
                    if kolichestvo == 201:
                        print(word, kolichestvo)