f = open('ege2/24/36037/24-3.txt').read()


f = f.replace('XZZY', ' ')
f = f.split()

max_posl = 0


for posl in f:
    max_posl = max(max_posl, len(posl) + 6)


print(max_posl)