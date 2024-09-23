f = open('ege3/24/27021/24.txt').read()



f = f.replace('A', ' ')

f = f.split()

max_len = 0


for posl in f:
    if 'B' not in posl:
        max_len = max(max_len, len(posl) + 2)



print(max_len)