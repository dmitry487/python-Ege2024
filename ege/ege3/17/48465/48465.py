f = open('ege3/17/48465/17-75.txt')



nums = [int(i) for i in f]


for num in sorted(nums):
    if abs(num)%10 == 6:
        kv_naim = num ** 2
        break


def check(num1, num2):
    if (
        (
            (abs(num1)%10 == 6) + (abs(num2)%10 == 6) == 1
        )and
        (
            (num1 ** 2 + num2 ** 2) < kv_naim
        )
    ):return True
    return False

kolichestvo = 0
max_sumkv = -200000


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sumkv = max(max_sumkv, nums[i] ** 2 + nums[j] ** 2)



print(kolichestvo, max_sumkv )