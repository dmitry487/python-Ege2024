f = open('ege3/9/abtask/1.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]



def check(row):
    nepovtor = []
    povtor = []
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)

        if row.count(num) > 1:
            povtor.append(num)


    if (
        (
            (len(set(row))) == 5
        )and
        (
            ((sum(povtor))/len(povtor)) < ((sum(nepovtor))/len(nepovtor))
        )
    ):return True
    return False



kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)
