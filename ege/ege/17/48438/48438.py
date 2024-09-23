f = open('ege/17/48438/17-8.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if str(num)[-1] == '7':
        kv_naim = num ** 2


def f(num1, num2):
    if(
        (
            ((num1%7 == 0) + (num2%7 == 0)) == 1
        ) and
        (
            ((num1**2) + (num2 ** 2)) < kv_naim
        )
    ): return True
    return False

kolichestvo = 0
max_sumkv = -20000


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_sumkv = max(max_sumkv, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, max_sumkv)