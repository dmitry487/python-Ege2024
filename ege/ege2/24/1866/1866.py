f = open('ege2/24/1866/24_1866.txt').read()

f = f.replace("ad", " ")
f = f.replace("da", ' ')

f = f.split()

max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl) + 2)


print(max_posl)