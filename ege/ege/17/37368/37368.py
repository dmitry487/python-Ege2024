f = open('ege/17/37368/17-5.txt')

nums = [int(i) for i in f]

def f(num1, num2):
    if (
        (
            (num1 + num2)%60 == 0
        )and
        (
            (num1%40 == 0) or (num2%40 == 0)
        )
    ): return True
    return False

kolichestvo =0
max_el = -1

for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1


            max_el = max(max_el,nums[i] + nums[j])

print(kolichestvo, max_el)