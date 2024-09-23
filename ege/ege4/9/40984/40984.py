f = open('ege4/9/40984/40984.txt')



nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    row = sorted(row)
    if (
        (
            ((row[0] * row[1]) + (row[0] * row[2]) > (row[1] * row[2]))
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)



3, 4, 100