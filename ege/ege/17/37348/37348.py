f = open('ege/17/37348/17-18.txt')


nums = [int(i) for i in f]


def f(num1, num2):
    if (
        (num1 * num2)%34 != 0
    ): return True
    return False

kolichestvo = 0
max_sum = - 1


for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])


print(kolichestvo, max_sum)