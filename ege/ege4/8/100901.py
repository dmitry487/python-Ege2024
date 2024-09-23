bad_combos = []
kolichestvo = 0
for i in '02468':
    for j in '02468':
        bad_combos.append(i + j)


for i in '1357':
    for j in '1357':
        bad_combos.append(i + j)

def check(num):
    for combos in bad_combos:
        if combos in num:
            return False
    return True
    


for a1 in '1234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                for a5 in '01234567':
                    num = a1 + a2 + a3 + a4 + a5
                    if ('1' not in num) and (check(num)) and (5 == len(set(num))):
                        kolichestvo += 1
                        
                    

print(kolichestvo)
                        


