f = open('ege/9/14/14.txt')

nums = [[int(i) for i in row.split()] for row in f]

def check(row):
    row = sorted(row)
    summ_povtor = 0
    for num in row:
        if row.count(num) > 1:
            summ_povtor += num

    if (
        (
            (len(set(row))) < 6
        )and 
        (
            (row.count(row[-1])) == 1
        )and
        (
            (summ_povtor < row[-1])
        )
    ): return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)