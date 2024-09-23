f = open('ege3/9/9/9.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    povtor = []

    for num in row:
        
            
        
        if row.count(num) == 2:
            povtor.append(num)


    if (
        (
            (len(povtor)) == 4
        )and
        (
            (sum(povtor)/ len(povtor)) < (sum(row)/len(row))
        )
    ):return True
    return False

kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)