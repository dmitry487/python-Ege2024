f = open('ege2/24/9845/24_9845.txt').read()

for i in "ABC":
    f = f.replace(i, '_')

for j in "89":
    f = f.replace(j, "*")

f = f.replace("_*", "))")
f = f.replace("_", ' ')
f = f.replace("*", ' ')


f = f.split()



max_combo = 0


for posl in f:
    max_combo = max(max_combo, len(posl))

print(max_combo)