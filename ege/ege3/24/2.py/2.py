f = open('ege3/24/2.py/24.txt').read()


for i in 'ABC':
    f = f.replace(i, '_')



for j in '6789':
    f = f.replace(j, '*')

f = f.replace('*_', ' ')
f = f.replace('_*', ' ')

f = f.split()

max_posl = 0
for posl in f: 
    max_posl = max(max_posl, len(posl) + 2)


print(max_posl)
