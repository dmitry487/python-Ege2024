f = open ('ege/17/57424/1_17.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if (num) in range (10, 100):
        max_el = num


def f(num1, num2):
    if (
        (
         ((num1) in range (10, 100)) + ((num2) in range (10, 100)) == 1
        )and
        (
            (num1 + num2)%max_el == 0
        )
    ): return True
    return False


kolichestvo = 0
max_sum = -200000

for i in range(len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])

print(kolichestvo, max_sum)