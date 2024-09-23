f = open('ege2/17/39746/17-50.txt')

nums = [int(i) for i in f]

def check(num1, num2, num3):
    if (
        (
            ((num1**2) == (num2 ** 2 + num3 ** 2)) or\
            ((num2**2) == (num1 ** 2 + num3 ** 2)) or\
            ((num3**2) == (num1 ** 2 + num2 ** 2))
        )
    ):return True
    return False

kolichestvo = 0
max_sum = 0

for i in range (len(nums) - 2):
    for j in range(i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1

                max_sum = max(max_sum,nums[i] + nums[j] + nums[k])


print(kolichestvo, max_sum)