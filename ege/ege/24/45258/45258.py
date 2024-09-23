f = open('ege/24/45258/107_24.txt').read()

f = f.replace('C', ' ')
f = f.replace('AB', '__')
f = f.replace('A', ' ')
f = f.replace('B', ' ')


f = f.split()

max_posl = 0
for posl in f:
    max_posl = max(max_posl, len(posl))
print(max_posl)

s = open('ege/24/45258/107_24.txt').read()

s = s.replace('AB', '-')
s = s.replace('CB', '_')
s = s.replace('C', ' ')
s = s.replace('B', ' ')
s = s.replace('A', ' ')
s = s.split()
max_drug = 0
for posl in s:
    max_drug = max(max_drug, len(posl))

print(max_drug)



