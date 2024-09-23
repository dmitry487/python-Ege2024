f = open('ege4/17/16328/17_16328.txt')


nums = [int(i) for i in f]

for num in sorted(nums):
    if num%19 == 0:
        min_el = num
        break

def check(num1, num2):
    if (
        (
            (num1%min_el == 0) + (num2%min_el == 0) >= 1
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