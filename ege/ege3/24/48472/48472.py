f = open('ege3/24/48472/24-13.txt').read()


f = f.replace('A', '_')
f = f.replace('O', '_')
f = f.replace('C', '*')
f = f.replace('D', '*')
f = f.replace('F', '*')
f = f.replace('__*', '+')
f = f.replace('_', ' ')
f = f.replace('*', ' ')

f = f.split()

max_posl = 0
for posl in f:
    max_posl = max(max_posl, len(posl))


print(max_posl)