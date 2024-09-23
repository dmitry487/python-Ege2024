f = open('ege/17/37361/17-27.txt')

nums = [int(i) for i in f]

def f(num1, num2):
    if (
        (
            (num1 + num2)%126 == 0
        )
    ): return True
    return False

kolichetvo = 0
max_sum = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichetvo += 1

            max_sum = max(max_sum, nums[i] + nums[j])

print(kolichetvo, max_sum)