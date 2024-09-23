f = open('ege/9/56537/56537.txt')


nums = [[int(i) for i in row.split()] for row in f]

def f(row):
    nepovtor = []
    povtor = []
    for num in row:
        if row.count(num) >1:
            povtor.append(num)
        elif row.count(num) == 1:
            nepovtor.append(num)
    
    if (
        (nepovtor and povtor) and
        (sum(nepovtor)/len(nepovtor)) < (sum(povtor)/len(povtor))
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if f(row):
        kolichestvo += 1

print(kolichestvo)

