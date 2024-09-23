f = open('ege2/9/12463/12463.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    nepovtor = []
    flag = True
    for num in row:
        if row.count(num) == 1:
            nepovtor.append(num)
        
    
    row = sorted(row)
    if ((sum(nepovtor))/3) < (row[-1]): flag = False

    for num in row:
        if row.count(num) != 4 or row.count(num) != 2: flag = False

    if flag:
        return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)