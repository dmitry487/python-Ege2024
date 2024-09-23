f = open('ege3/9/59714/59714.txt')



nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
        else:
            nepovtor.append(num)


    if (
         (
            (len(povtor)) == 4
         )and
         (
            ((sum(nepovtor))/len(nepovtor)) > ((sum(povtor))/(len(povtor)))
         )
    ):return True
    return False

kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)
