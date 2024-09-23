f = open('ege2/17/55604/17-47.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if str(num)[-1] == str(num)[-2]:
        kv_naim = num**2
        break

def check(num1, num2):
    if (
        (
            (str(num1)[-1]) == (str(num2)[-2]) or (str(num2)[-1]) == (str(num1)[-2])
        )and
        (
            (num1%7 == 0) + (num2%7 == 0) == 1
        )and
        (
            ((num1**2) + (num2 ** 2)) <= kv_naim
        )
    ):return True
    return False

kolichestvo = 0
max_vel = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_vel = max(max_vel, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, max_vel)