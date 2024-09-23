kolichestvo = 0
for a1 in 'xz':
    for a2 in 'xz':
        for a3 in 'abcde':
            for a4 in 'abcde':
                word= a1 + a2 + a3 + a4
                kolichestvo += 1

print(kolichestvo)