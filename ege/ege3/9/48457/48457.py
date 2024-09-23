f = open('ege3/9/48457/48457.txt')


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
            (len(povtor)) == 4 and (len(nepovtor)) == 2
        )and
        (
            sum(set(povtor)) > sum(nepovtor)
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)