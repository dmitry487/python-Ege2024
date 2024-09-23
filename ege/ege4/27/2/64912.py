f = open('ege4/27/2/27-B-2.txt')


nums = [int(i) for i in f]



def check(num1, num2, num3):
    if (
        (
            (num1 + num2 + num3)%102 == 0
        )
    ):return True
    return False


max_sum = 0


for i in range (len(nums) - 2):
    for j in range (i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            if check(nums[i], nums[j], nums[k]):
                max_sum = max(max_sum, nums[i] + nums[j] + nums[k])



print(max_sum)