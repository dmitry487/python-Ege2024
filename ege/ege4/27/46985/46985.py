f = open('ege4/27/46985/27-B-4.txt')

nums = [int(i) for i in f]

def check(num1, num2):
    if (
        (
            (num1 + num2)%999 == 0
        )
    ):return True
    return False

kolichestvo = 0


for i in range (len(nums) - 1):
    for j in range (i + 1, len(nums)):
        if check(nums[i], nums[j]):
            kolichestvo += 1


print(kolichestvo + 1)



#403 