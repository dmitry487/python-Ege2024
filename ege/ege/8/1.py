bad_combos = []
for i in '13579':
    for j in '13579':
        bad_combos.append(i + j)

for i in '02468':
    for j in '02468':
        bad_combos.append(i + j)



def check(num):
    for bad_word in bad_combos:
        if (bad_word in num) and (len(set(num)) != 5): return False
    return True
    




kolichestvo = 0
for a1 in '12345678':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                    num = a1 + a2 + a3 + a4 + a5
                    if num.count('1') > 0 and check(num):
                        kolichestvo += 1
print(kolichestvo)