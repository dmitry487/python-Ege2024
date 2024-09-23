f = open('ege3/9/1/2/2.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []
    nepovtor = []
    for num in row:
        if row.count(num) == 3:
            povtor.append(num)      
    for num in row:
        if row.count(num) == 1:
                nepovtor.append(num)
    if (
        (
            (len(set(row)) == 5) and (len(povtor) == 3)
        )and 
        (
           ((sum(nepovtor))//4) <= ((sum(povtor))//3)
        )
    ):return True
    return False

kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)