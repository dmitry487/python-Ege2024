f = open('ege/24/27691/zadanie24_1.txt').read()

f = f.replace('B', ' ')
f = f.replace('C', ' ')


f = f.split()
max_posl = 0
for posl in f:
    max_posl = max(max_posl, len(posl))

print(max_posl)