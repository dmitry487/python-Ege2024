f = open('ege/9/15/15.txt')

nums = [[int(i) for i in row.split()] for row in f]

def check(row):
    row = sorted(row)
    if (
        (
            ((row[0] * 6) < (row[1] + row[2] + row[3]) or (row[0] * 6) == (row[1] + row[2] + row[3]))
        )and 
        (
            (row[0] * row[-1]) > (row[1] * row[2])
        )
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)
