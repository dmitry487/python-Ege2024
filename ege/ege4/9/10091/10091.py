f = open('ege4/9/10091/10091.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        else:
            povtor.append(num)
    if (
        (
            (len(set(row))) == 5
        )and
        (
            (sum(povtor)//len(povtor)) < (sum(row)//len(row))
        )
    ):return True
    return False

kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)