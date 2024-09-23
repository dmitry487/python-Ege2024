f = open('ege2/9/59780/59780.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        if row.count(num) > 1:
            povtor.append(num)
    if (
        (
            (len(set(row))) == 4
        )and
        (
            ((sum(povtor))/4) < ((sum(row))/7)
        )
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)