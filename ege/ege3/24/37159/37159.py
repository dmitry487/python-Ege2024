f = open('ege3/24/37159/24-11.txt').read()


f = f.replace('a', '_')
f = f.replace('d', '_')
f = f.replace('__', ' ')


f = f.split()

max_len = 0
for posl in f:
    max_len = max(max_len, len(posl) + 2)



print(max_len)