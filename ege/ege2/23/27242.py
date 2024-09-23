res = [1]

for i in range (5):
    res_copy = res.copy()
    for num in res_copy:
        res += [num + 1, num * 2]


for i in range (1, 100):
    if i not in res:
        print(i)
        break