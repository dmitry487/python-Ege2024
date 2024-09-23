f = open('ege4/24/27691/zadanie24_1.txt').read()


f = f.replace('B', ' ')
f = f.replace('C', ' ')


f = f.split()

max_len = 0
for posl in f:
    max_len = max(max_len, len(posl))



print(max_len)