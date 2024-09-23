f = open('ege4/24/24/24_12254.txt').read()


f = f.replace('RSQ', '_')
f = f.replace('RS', '*')
f = f.replace('R', '{')
f = f.replace('SQ', '+')
f = f.replace('Q', '}')
f = f.replace('S', ' ')

f = f.split()

res = []
max_len = 0
for posl in f:
    for i in range(len(posl) - 2):
        if ((((((posl[0]) == '+') or (posl[0] == '}') or (posl[0] == '_')) or\
        (posl[-1] == '_') or (posl[-1] == '*') or (posl[-1] == '{'))) and(
            (posl[i + 2] != '+') and (posl[i + 2] != '}') and (posl[i + 2] != '*') and (posl[i + 2] != '{')
        )):
            if posl.count('_') == 17:
                print(posl)



s = '_______________{'

print(s.count('_') * 3)