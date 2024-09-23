f = open('ege2/9/59779/59779.txt')


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
            ((len(set(row))) == 5) or (len(set(row)) == 4)
        )and
        (
            (sum(povtor)/4) > (sum(nepovtor)/3)
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:    
    kolichestvo += 1


print(kolichestvo)