kolichestvo = 0

for a1 in 'матве':
    for a2 in 'матвей':
        for a3 in 'матвей':
            for a4 in 'матвей':
                for a5 in 'матвей':
                    for a6 in 'матвей':
                        word = a1 + a2 + a3 + a4 + a5 + a6
                        if 'ае' not in word:
                            kolichestvo += 1

                        

print(kolichestvo)