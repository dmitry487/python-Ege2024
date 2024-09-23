f = open('ege/24/27690/zadanie24_1.txt').read()

f = f.replace('CC', ' ')
f = f.replace('AA', ' ')
f = f.replace('BB', ' ')

f = f.split()
max_ = 0
for row in f:
    max_ = max(max_, len(row))

print(max_ + 2)
    
