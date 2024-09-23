f = open('ege/17/37371/17-45.txt')

nums = [int(i) for i in f]

def check(num1, num2):
    if (
        (
            (num1 - num2)%60 == 0
        )
    ): return True
    return False

kolichestvo = 0
max_razn = 0


for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_razn = max(max_razn, nums[i] - nums[j])


print(kolichestvo, max_razn)