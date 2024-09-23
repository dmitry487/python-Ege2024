f = open('ege3/27/35485/27-B.txt')


nums = [int(i) for i in f]
nums = sorted(nums,reverse=True)[:100]

print(nums)

def check(num1, num2, num3):
    if (num1 + num2 + num3)%3 == 0:
        return True
    return False

max_sum = 0


for i in range (len(nums) - 2):
    for j in range (i + 1, len(nums)):
        for k in range (j + 1, len(nums)):
            if check(nums[i], nums[j], nums[k]):
                max_sum = max(max_sum, nums[i] + nums[j] + nums[k])


print(max_sum)


