f = open('ege4/27/56527/27-B-3.txt')

nums = [int(i) for i in f]

def check(num1, num2):
    if (
        (
            (num1 + num2)%8 == 0
        )and
        (
            (num1 * num2)%2187 == 0
        )
    ):return True
    return False

kolichestvo = 0


for i in range (len(nums) - 1):
    for j in range (i + 18, len(nums)):
        if check(nums[i], nums[j]):
            kolichestvo += 1


print(kolichestvo)