kolichestvo = 0

def f(word):
    if (
        (
            (len(set(word)) == 6)
        ) and
        (
            ('еь' not in word) and ('яь' not in word)
        )
    ): return True
    return False

for a1 in 'демян':
    for a2 in 'демьян':
        for a3 in 'демьян':
            for a4 in 'демьян':
                for a5 in 'демьян':
                    for a6 in 'демьян':
                        word = a1 + a2 + a3 + a4 + a5 + a6

                        if f(word):
                            kolichestvo += 1
                    
print(kolichestvo)