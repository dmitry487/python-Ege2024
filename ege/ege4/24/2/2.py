f = open('ege4/24/2/24-15.txt').read()


f = f.replace('XZZY', ' ')

f = f.split()



max_posl = 0



for posl in f:
    max_posl = max(max_posl, len(posl) + 6)



print(max_posl)