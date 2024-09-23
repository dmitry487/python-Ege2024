f = open('ege/17/37341/17-3.txt')

nums = [int(i) for i in f]

max_el = -1
kolichestvo = 0

def f(num1, num2):
    if (
        (
            (num1 - num2)%2 == 0
        ) and 
        (
            (num1%19 == 0) or (num2%19 ==0)
        )
    ): return True
    return False

for i in range (len(nums) -1):
    for j in range (len(nums)):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_el = max(max_el, nums[i] + nums[j])

print(kolichestvo, max_el)