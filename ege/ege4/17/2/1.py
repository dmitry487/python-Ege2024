f = open('ege4/17/2/17-94.txt')


nums =[int(i) for i in f]

def check(num1, num2, num3, num4, num5, num6):
    if (
        (
            (num1 + num2) < (num2 + num3) > (num5 + num6)
        )and
        (
            ((num1 + num2) > 0) + ((num2 + num3) > 0) + ((num5 + num6) > 0) == 3
        )
    ):return True
    return False


kolichestvo = 0
min_pr  = 202020220202020202


for i in range (len(nums) - 5):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            for l in range (k + 1, k + 2):
                for p in range (l + 1, l + 2):
                    for o in range (p + 1, p + 2):
                        if check(nums[i], nums[j], nums[k], nums[l], nums[p], nums[o]):
                            kolichestvo += 1

                            min_pr = min(min_pr, nums[k] * nums[l])



print(kolichestvo, min_pr)


