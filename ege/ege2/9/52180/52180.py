f = open('ege2/9/52180/52180.txt')



nums = [
    [int(i) for i in row.split()] for row in f
]

print(nums)


def check(row):
    summa_chet = []
    summa_nechet = []
        
    for num in row:
        if num%2 == 0:
            summa_chet.append(num)

        if num%2 != 0:
            summa_nechet.append(num)


    if (
        (
            ((len(set(row)) == len(row)))
        )and
        (
            (len(summa_chet)) > (len(summa_nechet))
        )and
        (
            (sum(summa_chet)) < (sum(summa_nechet))
        )
    ):return True
    return False



kolichestvo = 0


for row in nums:
    if check(row):
        kolichestvo += 1



print(kolichestvo)