kolichstvo = 0
for a1 in 'белка':
    for a2 in 'белка':
        for a3 in 'белка':
            for a4 in 'белка':
                word = a1 + a2 + a3 + a4
                if word.count('б') == 1:
                    kolichstvo += 1

print(kolichstvo)
