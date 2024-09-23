f = open('kege/9/10121/10121.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []
    nepovtor = []
    kolichestvo = 0
    nekolichestvo = 0
    if (((len(set(row))) == (len(row)))): return False
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
            kolichestvo += 1
        elif row.count(num) == 1:
            nepovtor.append(num)
            nekolichestvo += 1
    
    if (((sum(povtor))/kolichestvo) < ((sum(nepovtor))/nekolichestvo)) and\
        ((len(set(row))) < (len(row))):return True
    return False

counter = 0

for row in nums:
    if check(row):
        counter += 1

print(counter)
