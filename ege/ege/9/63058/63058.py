f = open('ege/9/63058/63058.txt')

nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    povtor = []
    row = sorted(row)
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
        if (
            (
                len(set(row))) < (len(row)
            )and
            (
                row.count(row[-1]) == 1
            )and
            (
                (sum(povtor)) < row[-1]
            )
        ):return True
        return False
    
kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)