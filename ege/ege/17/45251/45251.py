f = open('ege/17/45251/107_17.txt')

nums = [int (i) for i in f]

for num in sorted(nums):
    if num%21 == 0:
        min_el = num

def f(num1, num2):
    if (
        (
            (num1%21 == 0) or (num2%21 == 0)
        )
    ):return True
    return False

kolichestvo = 0
max_summ  = -2000000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_summ = max(max_summ, nums[i] + nums[j])

print(kolichestvo, max_summ)