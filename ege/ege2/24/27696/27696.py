f = open('ege2/24/27696/zadanie24_2.txt').read()


f = f.replace('D', ' ')
f = f.replace('R', ' ')
f = f.replace('L', '_')

f = f.split()

max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl))


print(max_posl)