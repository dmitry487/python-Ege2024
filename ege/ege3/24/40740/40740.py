f = open('ege3/24/40740/24.txt').read()


f = f.replace('A', ' ')

f = f.split()

max_posl = 0
for posl in f:
    if posl.count('E') >= 3:
        max_posl = max(max_posl, len(posl))


print(max_posl)