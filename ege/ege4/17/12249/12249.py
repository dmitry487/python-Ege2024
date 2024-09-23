f = open('ege4/17/12249/17_12249.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if (
        (
            abs(num) in range (10000, 100000)
        )and
        (
            (abs(num))%10 == 3
        )
    ):max_el = num



def check(num1, num2, num3):
    if (
        (
            (abs(num1)%10 == 3) + (abs(num2)%10 == 3) + (abs(num3)%10 == 3) > 0
        )and
        (
            (num1 + num2 + num3) <= max_el
        )
    ):return True
    return False


kolichestvo = 0
max_sum = -100000000000000


for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1



                max_sum = max(max_sum, nums[i] + nums[j] + nums[k])



print(kolichestvo, max_sum)