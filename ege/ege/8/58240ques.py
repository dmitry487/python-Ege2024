from string import digits

alph = digits[:9]

bad_combos = set()

for i in '123456789':
    for j in '123456789':
        bad_combos.add(i + j)


def check(num):
    for i in bad_combos: return False
    return True


kolichestvo = 0

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    word = a1 + a2 + a3 + a4 + a5
                    if check(word):
                        kolichestvo += 1
            
        
print(kolichestvo)