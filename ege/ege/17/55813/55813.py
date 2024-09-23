f = open('ege/17/55813/17-35.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if num in range (100, 1000) and num%10 == 5:
        min_ = num
        break

def f(num1, num2):
    if (
        (
            (num1 in range (100, 1000)) + (num2 in range (100, 1000)) == 1
        )and
        (
            (num1 + num2)%min_ == 0
        )
    ): return True
    return False

kolichestvo = 0
min_sum = 100000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            min_sum = min(min_sum, nums[i] + nums[j])

print(kolichestvo, min_sum)