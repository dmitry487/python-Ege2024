f = open('ege/9/59802/59802.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        if row.count(num) >1:
            povtor.append(num)
    if (
        (
            len(povtor) == 4
        )and
        (
            len(nepovtor) == 3
        )and
        (
            (sum(nepovtor)/3)<(sum(povtor)/3)
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)