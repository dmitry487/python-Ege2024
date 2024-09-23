f = open('ege/9/11/11.txt')

nums = [[int(i) for i in row.split()] for row in f]

def check(row):
    if len(set(row)) != 4: return False
    row = sorted(row)

    summa_povtor  = set()
    summa_nepovtor = set()
    for num in row:
        if row.count(num) == 2:
            summa_povtor.add(num)
        elif row.count(num) == 1:
            summa_nepovtor.add(num)


        if (
            (
                (len(summa_povtor)) == 2 and (len(summa_nepovtor)) == 2 and (summa_povtor < summa_nepovtor)
            )
        ): return True
        return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)