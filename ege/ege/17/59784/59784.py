f = open('ege/17/59784/17-15.txt')

nums = [int(i) for i in f]


for num in sorted(nums):
    if abs(num)%100 == 25:
        max_el = num

def f(num1, num2, num3):
    if (
        (
            ((num1 in range (1000, 10000)) + (num2 in range (1000, 10000)) +\
            (num3 in range (1000, 10000))) == 1
        )and
        (
            (num1 + num2 + num3) < max_el
        )
    ):return True
    return False

kolichestvo = 0
min_sum = 2000000

for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if f(nums[i], nums[j], nums[k]):
                kolichestvo += 1



                min_sum = min(min_sum, nums[i] + nums[j] + nums[k])


print(kolichestvo, min_sum)