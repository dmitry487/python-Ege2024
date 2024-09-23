f = open('ege4/17/5/17-95.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if (
        (
            (abs(num)) in range (100, 1000)
        )
    ): kv_max = num ** 3



def check(num1, num2):
    if (
        (
           ((int((str(abs(num1)[0]))) + int(str(abs(num1)[1])) + int(str(abs(num1)[2])))%5 == 0) + 
            ((int(str(abs(num2)[0])) + int(str(abs(num2)[1])) + int(str(abs(num2)[2])))%5 == 0) == 1
        )and
        (
            abs(num1 - num2) >= kv_max
        )
    ):return True
    return False


kolichestvo = 0
max_sum = -234234923849203483290482


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1

            max_sum = max(max_sum, nums[i] + nums[j])



print(kolichestvo, max_sum)