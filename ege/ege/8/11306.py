kolichestvo = 0
for a1 in 'бронхи':
    for a2 in 'бронхи':
        for a3 in 'бронхи':
            for a4 in 'бронхи':
                word = a1 + a2 + a3 + a4
                if word.count('х') == 1:
                    kolichestvo += 1
print(kolichestvo)