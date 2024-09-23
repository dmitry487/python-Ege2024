f = open('ege/17/61363/17-36.txt')

nums = [
    int(i) for i in f
]

for num in sorted(nums):
    if num%100 == 19:
        max_el = num

def check(num1, num2, num3):
    if (
        (
            ((num1 in range (1000, 10000)) + (num2 in range (1000, 10000)) +\
            (num3 in range (1000, 10000))) == 2
        )and
        (
            (num1 % 3 == 0) or (num2 % 3 == 0) or (num3 % 3 == 0)
        )and
        (
            (num1 + num2 + num3) > max_el
        )
    ):return True
    return False

kolichestvo = 0
max_vel = 0


for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1

                max_vel = max(max_vel, nums[i] + nums[j] + nums[k])

print(kolichestvo, max_vel)