f = open('ege3/24/27693.py/zadanie24_1.txt').read()


f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.replace('C', '_')


f = f.split()

print(f)

max_posl = 0


for posl in f:
    max_posl = max(max_posl, len(posl))


print(max_posl)