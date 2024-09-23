f = open('ege3/9/1/1/1.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    row = sorted(row)
    if (
        (
            (row.count(row[-1])) == 1
        )and
        (
            (len(row)) != (len(set(row)))
        )and
        (
            row[-1] > ((row[0] + row[1] + row[2] + row[3] + row[4])/5)*3
        )
    ):return True
    return False
    

kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)