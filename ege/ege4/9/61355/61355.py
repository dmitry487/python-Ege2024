f = open('ege4/9/61355/61355.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    row = sorted(row)
    if (
        (
            (len(row)) == (len(set(row)))
        )and
        (
            (((row[-1]+ row[0]))//2) > (((row[1] +  row[2] +  row[3] + row[4]))//4)
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)