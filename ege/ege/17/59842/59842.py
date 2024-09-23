f = open('ege/17/59842/1777.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if abs(num)%100 == 29:
        max_el = num

def f(num1, num2, num3):
    if (
        (
            ((abs(num1) in range (10000, 100000)) + (abs(num2) in range (10000, 100000)) +\
            (abs(num3) in range (10000, 100000)) == 2)
        ) and
        (
            (num1 + num2 + num3) < max_el
        )
    ): return True
    return False

kolichestvo = 0
max_summ = -200000


for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if f(nums[i], nums[j], nums[k]):
                kolichestvo += 1


                max_summ = max(max_summ, nums[i] + nums[j] + nums[k])


print(kolichestvo, max_summ)