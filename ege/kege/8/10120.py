from string import digits, ascii_lowercase

alph = digits + ascii_lowercase[:7]
kolichestvo = 0

bad_combos = []
chet_combos = []

for i in '2468':
    chet_combos.append(i)

for i in '1':
    for j in '0246':
        chet_combos.append(i + j)
print(chet_combos)

def check(num):
    for good_num in chet_combos:
        if good_num in num:
            return True
        return False
    
for i in '1':
    for j in '135':
        bad_combos.append(i + j)

for i in '3579':
    bad_combos.append(i)





def check(num):
    for bad_num in bad_combos:
        if bad_num in num: return False
        return True

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    for a6 in alph:
                        num = a1 + a2 + a3 + a4 + a5 + a6
                        if (check(a1)) and (check(num)):
                            kolichestvo += 1

print(kolichestvo)