f = open('ege2/24/1205/24_1205.txt').read()

f = f.replace("G", " ")
f = f.replace("W", " ")
f = f.replace("P", " ")


f = f.split()

max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl))


print(max_posl)