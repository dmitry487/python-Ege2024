def  check(num1, num2, num3):
    if (
        (
            (num1 + num2 + num3)
        )
    ):return num1 + num2 + num3

max= 0
min = 0
for n in range (100, 100000):
    nums = [int(i) for i in n]
    for i in range (len(nums) - 2):
        for j in range (i + 1, i + 2):
            for k in range (j + 1, j + 2):
                if check(nums[i], nums[j], nums[k]):
                    max_ = max(max_, nums[i] + nums[j] + nums[k])
                    min_ = min(min_, nums[i] + nums[j] + nums[k])

                    r = max_ - min_

                    if r == 415:
                        print(n)
                        break
