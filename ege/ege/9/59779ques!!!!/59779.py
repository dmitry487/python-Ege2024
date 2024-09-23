f = open('ege/9/59779/59779.txt')

nums = [[int(i) for i in row.split()] for row in f]


def f(row):
    if (
        (
            (len(set(row)) == 4)
        )and
        (
            (row)
        )
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if f(row):
        kolichestvo += 1

print(kolichestvo)