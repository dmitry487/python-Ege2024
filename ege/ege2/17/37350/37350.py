f = open('ege2/17/37350/17-60.txt')


nums = [int(i) for i in f]


def check(num1, num2):
    if (
        (
            (num1 + num2) % 2 != 0
        )and
        (
            (num1 * num2)%3 == 0
        )
    ):return True
    return False


kolichestvo = 0
max_sum = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])

print(kolichestvo, max_sum)