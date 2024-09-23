f = open('ege/9/58517.py/58517.txt')


nums = [[int(i) for i in row.split()] for row in f]


def f(row):
    row = sorted(row)
    if (
        (
            (row.count(row[0])) == 1
        )and
        (
            (len(set(row))) < 6
        )and
        (
            (row[-1]) > ((row[0] + row[1] + row[2] + row[3])/5)
        )
    ):return True
    return False

kolichestvo = 0


for row in nums:
    if f(row):
        kolichestvo += 1

print(kolichestvo)