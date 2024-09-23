f = open('ege/17/39762/17-32.txt')

nums = [int(i) for i in f]



def f(num1, num2):
    if (
        (
            (num1 * num2) % 15 == 0
        )and
        (
            (num1 + num2) % 7 == 0
        )
    ): return True
    return False

kolichestvo = 0
max_sum = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        kolichestvo += 1


        max_sum = max(max_sum, nums[i] + nums[j])

print(kolichestvo, max_sum)