res = []

for x in range (1, 100):
    for y in range (1, 100):
        for z in range (1, 100):
            res.append([x, y, z])



def check(row):
    row = sorted(row)
    if (
        (
            ((row[-1] ** 2) > (row[0] ** 2 + row[1] ** 2))
        )and
        (
            (row[1]) == 25
        )and
        (
            (len(row)) == len(set(row))
        )
    ):return row[-1]/row[0], row[-1], row[0]
    return False


kolichestvo = 0
top = []
for row in res:
    if check(row):
        top.append(check(row))
        

print(min(top))



