

f = open('ege2/24/11813/24_11813.txt').read()


for i in "EYUIOA":
    f = f.replace(i, "_")


for j in "QWRTPSDFGHJKLZXCVBNM":
    f = f.replace(j, "*")


f = f.replace("_*", "))")
f = f.replace("*", " ")
f = f.replace("_", " ")


f = f.split()
print(f)
max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl))
    
print(max_posl + 1)


