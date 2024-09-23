f = open('ege4/17/16383/17_16383.txt')


nums = [int(i) for i in f]

for num in sorted(nums):
    if (abs(num)%100 == 21) and (abs(num) in range (10000, 100000)):
        kv_max = num ** 2


def check(num1, num2):
    if (
        (
            ((abs(num1)%100 == 21) and (abs(num1) in range (10000, 100000))) + 
            (((abs(num2))%100 == 21) and (abs(num2) in range (10000, 100000))) == 2
        )and
        (
            (num1 ** 2 + num2 ** 2) >= kv_max
        )
    ):return True
    return False


kolichestvo = 0
max_sum = -123123901231123


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])


print(kolichestvo, max_sum)