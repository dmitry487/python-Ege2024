f = open('ege/17/40733/17-43.txt')
nums = [int(i) for i in f]

for num in sorted(nums):
    sr_ar = (sum(nums)/5541)


def check(num1, num2):
    if (
        (
            (num1%3 == 0) or (num2%3 == 0)
        ) and
        (
            ((num1 > sr_ar) + (num2 > sr_ar) > 0)
        )
    ): return True
    return False

kolichestvo = 0
max_sum = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_sum = max(max_sum, nums[i], nums[j])

print(kolichestvo, max_sum)