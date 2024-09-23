f = open('ege/17/58484/17-13.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if (len(str(num)) == 3) and (abs(num)%10 == 5):
        naim = num

def f(num1, num2):
    if (
        (
            (len(str(num1)) == 4) + (len(str(num2)) == 4) == 1
        ) and
        (
            ((num1 ** 2) + (num2 ** 2))%naim == 0
        )
    ): return True
    return False

kolichestvo = 0
kv_sum = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            kv_sum = max(kv_sum, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, kv_sum)