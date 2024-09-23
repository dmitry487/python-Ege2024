f = open('ege/17/17/17.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if num%1000 == 123:
        max_el = num


def f(num1, num2, num3):
    if (
        (
            (num1 in range(10000, 100000)) + (num2 in range(10000, 100000)) + (num3 in range(10000, 100000)) >=2
        )and
        (
            (num1%10 == 3) + (num2%10 == 3) + (num3%10 == 3) == 1
        )and
        (
            (num1 + num2 + num3) > max_el
        )
    ): return True
    return False
kolichestvo = 0
max_vele = -200000

for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if f(nums[i], nums[j], nums[k]):
                kolichestvo += 1

                max_vele = max(max_vele, nums[i] + nums[j] + nums[k])

print(kolichestvo, max_vele)