f = open('ege3/17/2/17.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if num%100 == 15:
        min_el = num
        break


def check(num1, num2, num3):
    if (
        (
            (num1%100 == 15) or (num2%100 == 15) or (num3%100 == 15)
        )and
        (
            ((num1 ** 2) + (num2 ** 2) + (num3 ** 2)) >= min_el
        )
    ):return True
    return False


kolichestvo = 0
max_sum = 0


for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1


                max_sum = max(max_sum, nums[i] + nums[j] + nums[k])


print(kolichestvo, max_sum)
