f = open('ege/17/61397/17-31.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if abs(num)%100 == 17:
        max_el = num

def f(num1, num2, num3):
    if (
        (
            ((num1 in range (1000, 10000)) + (num2 in range (1000, 10000)) +\
            (num3 in range (1000, 10000))) == 2
        ) and
        (
            ((num1%5 == 0) + (num2%5 == 0) + (num3%5 == 0)) > 0
        ) and
        (
            (num1 + num2 + num3) > max_el
        )
    ): return True
    return False

kolichestvo = 0
max_vel = -200000

for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if f(nums[i], nums[j], nums[k]):
                kolichestvo += 1

                max_vel = max(max_vel, nums[i] + nums[j] + nums[k])

print(kolichestvo, max_vel)