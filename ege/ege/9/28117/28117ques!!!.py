f = open('ege/9/28117/28117.txt')

nums = [[float(str(i.replace(',', '.'))) for i in row.split()] for row in f]

def f(row):
    for num in row:
        if (
        (sum(num)%(len(row)) <= 20)
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if f(row):
        kolichestvo += 1

print(kolichestvo)