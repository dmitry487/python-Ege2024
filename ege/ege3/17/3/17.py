f = open('ege3/17/3/17.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if num%1000 == 538:
        max_el = num



def check(num1, num2, num3, num4):
    if (
        (
            ((num1 in range (10000, 100000)) + (num2 in range (10000, 100000)) +
            (num3 in range (10000, 100000)) + (num4 in range (10000, 100000)) > 1) and 
            ((num1 not in range (10000, 100000)) + (num2 not  in range (10000, 100000)) +
            (num3 not in range (10000, 100000)) + (num4 not in range (10000, 100000)) > 0)
        )and
        (
            ((num1%3 == 0) + (num2%3 == 0) + (num3%3 == 0) + (num4%3 == 0)) >
            ((num1%7 == 0) + (num2%7 == 0) + (num3%7 == 0) + (num4%7 == 0))
        )and
        (
            ((num1 + num2 + num3 + num4) > max_el) and ((num1 + num2 + num3 + num4) < (max_el * 2))
        )
    ):return True
    return False


kolichestvo = 0
max_vel = 0


for i in range (len(nums) - 3):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            for p in range (k + 1, k + 2):
                if check(nums[i], nums[j], nums[k], nums[p]):
                    kolichestvo += 1


                    max_vel = max(max_vel, nums[i]+ nums[j] + nums[k] + nums[p])



print(kolichestvo, max_vel)