f = open('ege4/24/16333/24_16333.txt').read()


for i in '124':
    f = f.replace(i, '_')


for i in 'QRW':
    f = f.replace(i, '*')

f = f.replace('__', ' ')
f = f.replace('**', ' ')
f = f.split(' ')
max_len = 0

for posl in f:
    max_len =  max(max_len, len(posl))
 



print(max_len + 1)
