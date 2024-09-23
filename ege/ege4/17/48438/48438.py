f = open('ege4/17/48438/17-97.txt')
nums = [int(i) for i in f]

for num in sorted(nums):
    if abs(num)%10 == 7:
        kv_naim = num ** 2
        break



def check(num1, num2):
    if (
        (
            (abs(num1)%10 == 7) + (abs(num2)%10 == 7) == 1
        )and
        (
            (num1 ** 2 + num2 ** 2) < kv_naim
        )
    ):return True
    return False

kolichestvo = 0
max_sumkv = -2838203489023849023894029348


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_sumkv = max(max_sumkv, nums[i] ** 2 + nums[j] ** 2)



print(kolichestvo, max_sumkv)