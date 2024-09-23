f = open('ege3/17/39762/17-76.txt')


nums = [int(i) for i in f]


def check(num1, num2):
    return (
        (
            (num1 * num2)%15 == 0
        )and
        (
            (num1 + num2)%7 == 0
        )
    )

kolichestvo = 0
max_sum = 0


for i in range (len(nums) - 1):
    for j in range (i + 1, i + 2):
        if check(nums[i], nums[j]):
            kolichestvo += 1


            max_sum = max(max_sum, nums[i] + nums[j])

    
print(kolichestvo, max_sum)