kolichestvo = 0

def f(num):
    if ('61' not in num) and ('63' not in num) and ('65' not in num) and\
    ('67' not in num) and ('69' not in num) and ('16' not in num) and\
    ('36' not in num) and ('56' not in num) and ('76' not in num) and\
    ('96' not in num): return True
    return False
    


for a1 in '01234567':
    for a2 in '01234567':
        for a3 in '01234567':
            for a4 in '01234567':
                for a5 in '01234567':
                    num = a1 + a2 + a3 + a4 + a5
                    if num.count('6') == 1 and f(num):
                        kolichestvo += 1

print(kolichestvo)