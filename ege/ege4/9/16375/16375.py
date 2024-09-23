f = open('ege4/9/16375/16375.txt')


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
    povtor = sorted(povtor)
    nepovtor = sorted(nepovtor)
    if (
        (
            ((len(povtor)) == 2) and ((len(nepovtor)) == 5)
        )and
        (
            (nepovtor[0] * nepovtor[1] * nepovtor[2]) > (povtor[0] * povtor[1])
        )
    ):return True
    return False

kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)