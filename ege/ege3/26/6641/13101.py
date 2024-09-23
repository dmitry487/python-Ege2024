f = open('ege3/26/6641/26_6641.txt').readlines()


n = 9880
m = 395200

s = []
w = []

for i in f:
    row = i.split()
    price, tip = int(row[0]), row[1]
    
    if tip == 'S':
        s.append(price)
    else:
        w.append(price)

    
s = sorted(s)
w = sorted(w)


max_sum = 0

print(len(s), len(w))

print(sum(s[:700]), sum(w[:700]))

obsh = []
for i in range (0, 700):
    for j in range (0, 700):
        s_money = sum(s[:i])
        w_money = sum(w[:j])   
        if (s_money + w_money <= m):
            obsh.append([
                i + j, i, m - s_money - w_money
            ])

print(sorted(obsh)[-10:])

