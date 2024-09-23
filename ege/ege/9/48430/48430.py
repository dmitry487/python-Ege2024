lines = open('ege/9/48430/48430.txt')


data = [list(map(int, line.split())) for line in lines]
count = 0
for row in data:
    st4, st_not_4 = set(), set()
    for item in row:
        if row.count(item) == 4:
            st4.add(item)
        else:
            st_not_4.add(item)
    if len(st4) == 1 and sum(st4) > sum(st_not_4) / len(st_not_4):
        count += 1
print(count)