f = open('ege/17/59722/1_17.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if num%100 == 17:
        naib = num
    
def check(num1, num2, num3):
    if (
        (
            ((num1 in range (100, 1000)) + (num2 in range (100, 1000)) +\
            (num3 in range (100, 1000))) == 1
        )and
        (
            (num1 + num2 + num3) < naib
        )
    ): return True
    return False

kolichestvo = 0

for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1


print(kolichestvo)