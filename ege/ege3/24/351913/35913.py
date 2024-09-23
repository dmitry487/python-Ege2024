from string import ascii_uppercase

alph = ascii_uppercase

f = open('ege3/24/351913/24-14.txt').readlines()

min_len = 1000000000000000000000000000
max_letter = 0
res = []
for posl in f:
    
    
    if posl.count('N') == 23:
        res.append(posl)
        

res = res[0]
print(res)
max_letter = 0
for i in alph:
    max_letter = max(max_letter, res.count(i))


    if res.count(i) == 53:
        print(i)
    