f = open('ege2/9/58476/58476.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    row = sorted(row)

    if (row.count(row[-1]) == 1) and\
    ((len(set(row))) != len(row)) and\
   ((row[-1]) > 3 * ((row[0] + row[1] + row[2] + row[3] + row[4])/5)):
        return True
    return False

kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)