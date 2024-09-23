bad_combos = set()
for i in ('ая'):
    for j in ('ая'):
        bad_combos.add(i + j)
for i in ('нст'):
    for j in ('нст'):
        bad_combos.add(i + j)

def check(num):
    if (len(set(num))) != 4: return False
    for i in bad_combos:
        if i in num: return False
    return True
        
kolichestvo = 0

for a1 in 'настя':
    for a2 in 'настя':
        for a3 in 'настя':
            for a4 in 'настя':
                word = a1 + a2 + a3 + a4
                kolichestvo += 1
                kolichestvo += check(word)

print(kolichestvo)