f = open('ege/17/37372/17-28.txt')

nums = [int(i) for i in f]

def f(num1, num2):
    if (
        (
            (num1 - num2) % 45 == 0
        )and
        (
            ((num1 % 18 == 0) + (num2 % 18 == 0)) == 1
        )
    ): return True
    return False

kolichestvo = 0
max_razn = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_razn = max(max_razn, nums[i] - nums[j])
print(kolichestvo, max_razn)