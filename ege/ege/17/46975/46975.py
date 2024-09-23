f = open('ege/17/46975/17-17.txt')


nums = [int(i) for i in f]

spis = []

for num in sorted(nums):
    if num%2 == 0:
        spis.append(num)

sr_znach = (sum(spis) / len(spis))

def f(num1, num2):
    if ((num1 % 3 == 0) and (num2 < sr_znach)) or\
          ((num2 % 3 == 0) and (num1 < sr_znach)): 
         return True
    return False

kolichestvo = 0
max_sum = -1

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_sum = max(max_sum, nums[i] + nums[j])

print(kolichestvo, max_sum)

