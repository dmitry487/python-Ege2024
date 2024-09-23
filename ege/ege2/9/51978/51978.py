f = open('ege2/9/51978/51978.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    if len(set(row)) == len(row): return True
    chet = []
    nechet = []
    n = 0
    c = 0
    for num in row:
        if num%2 == 0:
            c += 1
            chet.append(num)
        elif num%2 != 0:
            n += 1
            nechet.append(num)
        if (
            (
                (n < c)
            )and
            (
                (sum(chet)) > (sum(nechet))
            )
        ):return True
        return False

        
kolichestvo = 0

for row in nums:
    if check(row):
        kolichestvo += 1

print(kolichestvo)