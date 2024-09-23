f = open('ege4/26/59776/59776.txt')

day = 1300

nums = [
    [int(i) for i in row.split()] for row in f
]
res = []
sum = 13
for num in nums:
    if num[0] == sum:
        sum = num[0] + num[1]

        day -= sum
        res.append(sum)

print(res)
print(len(res))