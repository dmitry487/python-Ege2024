f = open('ege/9/12/12.txt')

nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    row = sorted(row)

    if (
        ((len(set(row))) == 5) and
        ((row[0] + row[-1]) * 2) <= (row[1] + row[2] + row[3])
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)