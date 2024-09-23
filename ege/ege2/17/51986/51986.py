f = open('ege2/17/51986/17-49.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if str(num)[-1] == '5':
        kv_naim = num**2
        break

def check(num1, num2):
    if (
        (
            (num1 < num2) and (str(num1)[-1] == '5') or\
            (num2 < num1) and (str(num2)[-1] == '5')
        )and
        (
            (num1 ** 2 + num2 ** 2) < kv_naim
        )
    ):return True
    return False

kolichestvo = 0
max_sumkv = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_sumkv = max(max_sumkv, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, max_sumkv)