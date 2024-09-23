f = open('ege4/24/27698/zadanie24_2.txt').read()

f = f.replace('L', ' ')
f = f.replace('D', ' ')


f = f.split(' ')
max_len = 0

for posl in f:
    if len(posl) == 2:
        print(posl)


#otvet - 1