f = open('ege3/24/38602.py/24-12.txt').read()


f = f.replace('PP', ' ')

f = f.split()


max_len = 0


for posl in f:
    max_len = max(max_len, len(posl) + 2)



print(max_len)