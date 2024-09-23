f = open('ege/17/40992/17-37.txt')

nums = [int(i) for i in f]


sr_ar = sum(nums)//len(nums)

def check(num1, num2):
    if (
        (
            (num1 % 5 == 0) or (num2 % 5 == 0)
        )and
        (
            (num1 < sr_ar) or (num2 < sr_ar)
        )
    ): return True
    return False

kolichestvo = 0
max_sum = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_sum = max(max_sum, nums[i] + nums[j])

print(kolichestvo, max_sum)