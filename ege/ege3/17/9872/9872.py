f = open('ege3/17/9872/17_9872.txt')


nums = [int(i) for i in f]


def to13(num: int):
    digits = ''
    while num > 0:
        digits += str(num%13)
        num //= 13
    return digits[::-1]

for num in sorted(nums):
    num13 = to13(num)
    if str(num13)[-2:] == '12':


        max_el = num

def check(num1, num2, num3):
    if (
        (
            (num1 in range (100, 1000)) + (num2 in range (100, 1000)) +
            (num3 in range (100, 1000))
        )and
        (
            (num1 + num2 + num3) < max_el
        )
    ):return True
    return False


kolichestvo = 0
max_p = -2000000

for i in range (len(nums) - 2):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            if check(nums[i], nums[j], nums[k]):
                kolichestvo += 1


                max_p = max(max_p, nums[i] * nums[j] * nums[k])



print(kolichestvo, max_p)




