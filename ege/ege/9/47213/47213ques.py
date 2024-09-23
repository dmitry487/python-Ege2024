f = open('ege/9/47213/47213.txt')


nums = [[int(i) for i in row.split()] for row in f]


def f(row):
    nepovtor = []
    povtor = []
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
        else:
            nepovtor.append(num)
    if (
        (
            (len(set(row))) == 5
        )and
        (
            (sum(nepovtor)/len(nepovtor)) <= (sum(povtor))
        )
    ):return True
    return False


kolichestvo = 0
for row in nums:
    if f(row):  
        kolichestvo += 1


print(kolichestvo)