f = open('ege3/9/52180/52180.txt')

nums = [
    [int(i) for i in row.split()] for row in f
]


def check(row):
    chet = []
    nechet = []
    for num in row:
        if num%2 == 0:
            chet.append(num)
        else:
            nechet.append(num)
    if (
        (
            (len(set(row))) == len(row)
        )and
        (
            (len(chet)) > (len(nechet))
        )and
        (
            (sum(chet)) < (sum(nechet))
        )
    ):return True
    return False


kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)