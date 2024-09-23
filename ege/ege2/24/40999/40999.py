f = open('ege2/24/40999/24.txt').read()


f = f.replace('E', " ")
f = f.split()
print(f)

max_posl = 0
for posl in f:
    if posl.count('A') >= 3:
        max_posl = max(max_posl, len(posl))



print(max_posl)