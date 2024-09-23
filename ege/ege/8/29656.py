def check(word):
    if  (
        (
            (word.count('а')) == 1 and (word.count('й')) == 1
        )
    ):return True
    return False


kolichestvo = 0

for a1 in 'андре':
    for a2 in 'андрей':
        for a3 in 'андрей':
            for a4 in 'андрей':
                for a5 in 'андрей':
                    for a6 in 'андрей':
                        for a7 in 'андрей':
                            word = a1 + a2 + a3 +\
                                  a4 + a5 + a6 + a7
                            
                            if check(word):
                                kolichestvo += 1

print(kolichestvo)