f = ('ege3/27/27989/27989_A.txt')



nums = [int(i) for i in f]


def check(num1, num2):
    if (
        (
            (num1 * num2)%26 == 0
        )
    ):return True
    return False


kolichestvo = 0


for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if check(nums[i], nums[j]):
            kolichestvo += 1


print(kolichestvo)