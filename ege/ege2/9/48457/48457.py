f = open('ege2/9/48457/48457.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = set()
    nepovtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        if row.count(num) > 1:
            povtor.add(num)

    if (
        (
            (len(set(row)) == 4) and (len(set(row)) < len(row))
        )and
        (
            (sum(povtor)) > (sum(nepovtor))
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)