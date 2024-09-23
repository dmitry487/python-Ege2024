f = open('ege3/24/27688/24_demo.txt').read()



f = f.replace('X', ' ')
f = f.replace('Y', ' ')
f = f.replace('Z', '_')


f = f.split()


max_posl = 0


for posl in f:
    max_posl = max(max_posl, len(posl))


print(max_posl)