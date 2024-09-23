f = open('ege/17/56517/17-22.txt')

nums = [int(i) for i in f]


for num in sorted(nums):
    if str(num)[-1] == '3':
        kv_naim = num**2

def f(num1, num2):
    if (
        (
            ((str(num1)[-1]) == (str(num2)[-1]))
        )and
        (
            (num1%3 == 0) + (num2%3 == 0) == 1
        )and
        (
            (num1 ** 2 + num2 ** 2) < kv_naim
        )
    ): return True
    return False


kolichestvo = 0
max_kv = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_kv = max(max_kv, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, max_kv)