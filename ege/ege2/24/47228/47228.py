f = open('ege2/24/47228/24-5.txt').read()

f = f.replace('AO', ' ')
f = f.replace('CDF', ' ')
f = f.replace('CD', ' ')
f = f.replace('DF', ' ')
f = f.replace('A', '-')
f = f.replace('O', '-')
f = f.replace('C', '*')
f = f.replace('D', '*')
f = f.replace('F', '*')


f = f.split()
max_posl = 0

def check(posl):
    if ('***' not in posl and '**' not in posl and '--' not in posl and\
    '---' not in posl) and (('*-' in posl) or ('-*' in posl)): return True
    return False

for posl in f:
    if check(posl):
        max_posl = max(max_posl, posl.count('*-') + 5)
        print(posl)


print(max_posl)