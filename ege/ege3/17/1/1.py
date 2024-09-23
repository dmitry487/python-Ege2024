f = open('ege3/17/1/17-73.txt')


nums = [int(i) for i in f]

for num in sorted(nums):
    if (abs(num))%1000 == 221:
        max_el =num



def check(num1, num2, num3):
    if (
        (
            (abs(num1) > 9) + (abs(num2) > 9) +\
            (abs(num3) > 9) == 2
        )and
        (
            (abs(num1) in range (10, 100)) + (abs(num2) in range (10, 100)) +\
            (abs(num3) in range (10, 100)) <= 2
        )and
        (
            (num1 + num2 + num3) > max_el
        )
    ):return True
    return False

min_sum = 2000000
kolichestvo = 0


for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1


                min_sum = min(min_sum, nums[i] + nums[j] + nums[k])
                

print(kolichestvo, min_sum)