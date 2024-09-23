f = open('ege/9/39238/39238.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def f(row):
    row = sorted(row)
    if (
        (
            (row[-1]**2) == ((row[0] ** 2) + (row[1] ** 2))
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if f(row):
        kolichestvo += 1


print(kolichestvo)