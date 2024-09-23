f = open('ege4/24/15339/24_15339.txt').read()

for i in '6789':
    f = f.replace(i, '_')


for j in 'ABC':
    f = f.replace(j, '*')


f = f.replace('___', ' ')
f = f.replace('**', ' ')



f = f.split()

max_len = 0
for posl in f:
    print(posl)