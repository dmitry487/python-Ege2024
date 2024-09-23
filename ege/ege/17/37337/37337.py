f = open('ege/17/37337/17-6.txt')

nums = [int(i) for i in f]

def f(num1, num2):
    if (
        (
            (num1%160) != (num2%160)
        )and
        (
            (num1%7 == 0) or (num2%7 == 0)
        )
    ): return True
    return False

kolichestvo = 0
max_el = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_el = max(max_el, nums[i] + nums[j])

print(kolichestvo, max_el)