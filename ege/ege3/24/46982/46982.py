f = open('ege3/24/46982/24.txt').read()



f = f.replace('E', ' ')
f = f.split()




kolichestvo = 0
for posl in f:
    if ('F' not in posl) and (len(posl) + 2 >= 12):
        kolichestvo += 1
        
        


print(kolichestvo)