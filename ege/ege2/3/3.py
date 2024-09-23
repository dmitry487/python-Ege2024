f = open('ege2/3/3.txt')

res = {i:0 for i in range (110)}

for row in f:
    row = row.split()
    money, magaz = int(row[0]), int(row[1][1:]) 
    res[magaz] += money

max_sum = 0
for i in res:
    max_sum = max(max_sum, res[i])

print(max_sum)

