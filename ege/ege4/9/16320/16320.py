f = open('ege4/9/16320/16320.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    row = sorted(row)


    if (
        (
            (row[-1]) < (row[0] + row[1] + row[2])
        )and
        (
            ((row[1] + row[2]) == (row[0] + row[3])) or
            (((row[1]) + row[3]) == (row[0] + row[2]))
        )
    ):return True
    return False


kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)