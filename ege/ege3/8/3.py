bad_combos = []

for i in '24680':
    for j in '24680':
        bad_combos.append(i + j)

for i in '1357':
    for j in '1357':
        bad_combos.append(i + j)


def check(word):
    for bad_word in bad_combos:
        if (bad_word in word): return False
    return True

kolichestvo = 0

for a1 in '12345678':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                        word = a1 + a2 + a3 + a4 + a5
                        if (
                            check(word)
                        ) and ((len(set(word))) == (len(word))) and ((word.count('1')) > 0):
                            kolichestvo += 1

print(kolichestvo)