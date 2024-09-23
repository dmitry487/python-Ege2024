f = open('ege2/24/1230/24_1230.txt').read()


f = f.replace("W", " ")
f = f.replace("R", " ")
f = f.replace("Q", " ")

f = f.split()

max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl))

print(max_posl)