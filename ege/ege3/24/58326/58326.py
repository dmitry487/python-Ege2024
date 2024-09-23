import sys
sys.set_int_max_str_digits(150000)

f = open('ege3/24/58326/24_5832.txt')

nums = [int(i) for i in f]

def check(num1, num2):
    if num1 >= num2:
        return True
    return False

max_len = 0

for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            max_len = max(max_len, i + 1)


print(max_len)
