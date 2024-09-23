kolichestvo = 0

bad_combo = []

for i in '0246':
    for j in '0246':
        bad_combo.append(i + j)


for i in '1357':
    for j in '1357':
        bad_combo.append(i + j)


def check(word):
    for combo in bad_combo:
        if combo in word:
            return False
        
    return True    


for w1 in '1234567':
    for w2 in '01234567':
        for w3 in '01234567':
            for w4 in '01234567':
                for w5 in '01234567':
                    word = w1 + w2 + w3 + w4 + w5

                    if ('1' not in word) and (len(set(word)) == 5) and\
                    check(word):
                        kolichestvo += 1


print(kolichestvo)

