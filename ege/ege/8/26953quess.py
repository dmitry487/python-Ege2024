bad_combos = []

for i in '13579':
    for j in '13579':
        bad_combos.append(i + j)

for i in '02468':
    for j in '02468':
        bad_combos.append(i + j)

kolichestvo = 0
for a1 in '01234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                for a5 in '01234567':
                    num = a1 + a2 + a3 + a4 + a5
                    if num.count('0') == 1 and num.count('1') == 1 and num.count('2') == 1 and\
                        num.count('3') == 1 and num.count('4') == 1 and num.count('5') == 1 and\
                            num.count('6') == 1 and num.count('7') == 1 and bad_combos not in num:
                            kolichestvo += 1
                        
print(kolichestvo)
                
