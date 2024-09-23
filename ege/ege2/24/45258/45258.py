f = open('ege2/24/45258/107_24.txt').read()



f = f.replace("AB", "_")
f = f.replace("CB", "*")
f = f.replace('C', ' ')
f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.split()


max_len = 0
for posl in f:
    if '_' in posl and '*' not in posl:
        max_len = max(max_len, len(posl))


print(max_len)