f = open('ege3/9/55805/55805.txt')



nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    row = sorted(row)
    if (
        (
            (len(set(row))) == len(row)
        )and
        (
            (row[-1] + row[0]) * 3 <= (row[1] + row[2] + row[3]) * 2
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)