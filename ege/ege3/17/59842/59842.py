f = open('ege3/17/59842/59842.txt')


nums = [
    [int(i) for i in row.split()] for row in f
]


for num in sorted(nums):
    if abs(num)%100 == 29:
        print(num)