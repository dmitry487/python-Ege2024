f = open('ege/17/37349/17-7.txt')

nums = [int(i) for i in f]

def f(num1, num2):
    if (
        (
            (num1 * num2)%26 == 0
        )
    ): return True
    return False

kolichestvo =0
max_el = -20000

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_el = max(max_el, nums[i] + nums[j])

print(kolichestvo, max_el)