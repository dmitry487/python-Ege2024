f = open('ege3/17/63066/17.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if num%1000 == 321:
        max_el = num
        


def check(num1, num2, num3):
    if (
        (
            (num1 in range (100_00, 100_000)) + (num2 in range (100_00, 100_000)) +\
            (num3 in range (100_00, 100_000)) == 2
        )and
        (
            (num1%5 == 0) or (num2 %5 == 0) or (num3 %5 == 0)
        )and
        (
            (num1 + num2 + num3) > max_el
        )
    ):return True
    return False


kolichestvo = 0
max_vel = 0


for i in range (1, len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1


                max_vel = max(max_vel, nums[i] + nums[j] + nums[k])



print(kolichestvo, max_vel)