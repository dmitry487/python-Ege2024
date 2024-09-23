kolichestvo = 0
for a1 in 'еэ':
    for a2 in 'егэ':
        for a3 in 'егэ':
            for a4 in 'егэ':
                for a5 in 'егэ':
                    word = a1 + a2 + a3 + a4 + a5
                    kolichestvo += 1

print(kolichestvo)