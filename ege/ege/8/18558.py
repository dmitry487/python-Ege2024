kolichestvo = 0
for a1 in 'иван':
    for a2 in 'иван':
        for a3 in 'иван':
            for a4 in 'иван':
                for a5 in 'иван':
                    word = a1 + a2 + a3 + a4 + a5
                    if word.count('и') > 0:
                        kolichestvo += 1
print(kolichestvo)
