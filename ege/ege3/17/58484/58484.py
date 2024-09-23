f = open('ege3/17/58484/17-85.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if (num%10 == 5) and (num in range (100, 1000)):
        naim = num
        break



def check(num1, num2):
    if (
        (
            (num1 in range (1000, 10000)) + (num2 in range (1000, 10000)) == 1
        )and
        (
            (num1 ** 2 + num2 ** 2)%naim == 0
        )
    ):return True
    return False


kolichestvo = 0
max_sum = 0


for i in range (len(nums) - 1):
    for j in range(i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] ** 2 + nums[j] ** 2)



print(kolichestvo, max_sum)