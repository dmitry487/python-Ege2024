f = open('ege2/9/56509/56509.txt')


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
    if (len(nepovtor) == 0) or (len(povtor) == 0): return False

    if (
        
        (
            (sum(nepovtor)/len(nepovtor)) > (sum(povtor)/len(povtor))
        )
    ):return True
    return False

kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)