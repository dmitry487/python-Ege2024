f = open('ege4/17/15333/17_15333.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if num%19 == 0:
        max_el = num



def check(num1, num2):
    if (
        (
            (num1 > max_el) + (num2 > max_el) >= 1
        )
    ):return True
    return False


kolichestvo = 0
max_sum = 0


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])



print(kolichestvo, max_sum)