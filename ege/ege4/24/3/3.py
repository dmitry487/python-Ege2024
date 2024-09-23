f = open('ege4/24/3/24-16.txt').read()

f = f.replace('ABA', '_')
f = f.replace('BAB', '_')
f = f.replace('C', ' ')
f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.split(' ')

max_posl = 0
for posl in f:
    max_posl = max(max_posl, len(posl))
    

print(max_posl)

              