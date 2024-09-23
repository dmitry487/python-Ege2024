f = open('ege/9/45243/45243.txt')

nums = [[int(i) for i in row.split()] for row in f]

def check(row):
    row = sorted(row)
    if (
        (
            ((row[-1] + row[0])**2) > (row[1] ** 2 + row[2] ** 2 + row[3] ** 2)
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)