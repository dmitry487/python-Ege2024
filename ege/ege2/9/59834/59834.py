f = open('ege2/9/59834/59834.txt')
nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    povtor = set()
    nepovtor = set()
    for num in row:
        if row.count(num) > 1:
            povtor.add(num)
        if row.count(num) == 1:
            nepovtor.add(num)
    if (
        (
            (len(set(row)) == 5)
        )and
        (
            ((sum(povtor))/2) < ((sum(nepovtor))/4)
        )
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)

