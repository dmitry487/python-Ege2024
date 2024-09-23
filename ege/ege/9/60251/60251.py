f = open('ege/9/60251/60251.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]

def check(row):
    povtor = []
    for num in row:
        if row.count(num) > 1:
            povtor.append(num)

    if (
        ((len(set(row))) == 5) and\
        (sum(povtor)/5) < (sum(row)/7)
    ):return True
    return False

kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)