f = open('ege3/24/1/24_9845.txt').read()


f = f.replace('A', '_')
f = f.replace('B', '_')
f = f.replace('C', '_')
f = f.replace('8', '*')
f = f.replace('9', '*')
f = f.replace('__', ' ')
f = f.replace('**', ' ')
f = f.split(' ')


max_posl = 0

for posl in f:
    max_posl = max(max_posl, len(posl))



print(max_posl + 1)