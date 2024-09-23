f = open('ege2/17/47014/17-51.txt')

nums = [int(i) for i in f]
summ = 0
kolichestvo = 0
for num in sorted(nums):
    if num%2 != 0:
        kolichestvo += 1
        summ += num
    
res = summ/kolichestvo


def check(num1, num2):
    if (
        (
            ((num1%5 == 0) and (num2 < res)) or ((num1 < res) and (num2%5 == 0))
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
    
