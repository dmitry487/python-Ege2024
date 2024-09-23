def check(word):
    if (
        (
            (word.count('с')) >= 1
        )
    ): return True
    return False

kolichestvo =0


for a1 in 'света':
    for a2 in 'света':
        for a3 in 'света':
            for a4 in 'света':
                for a5 in 'света':
                    word = a1 + a2 + a3 + a4 + a5

                    if check(word):
                        kolichestvo += 1

print(kolichestvo)