nums = []
for i in range (1, 341):
    nums.append(i)
    
    



def check(num1, num2, num3, num4):
    if (
        (
            (num1) %3 != 0
        )and
        (
            (num2)%3 != 0
        )and
        (
            (num3)%3 !=0
        )and
        (
            (num4)%3 != 0
        )
        (
            (num1 + num2 + num3 + num4) == 240
        )
    ):return True
    return False






for i in range (len(nums) - 3):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            for p in range (k + 1, k + 2):
                if check(nums[i], nums[j], nums[k], nums[p]):
                    print('да')
                else:
                    print('нет')


print('---------------------')



nums = []
for i in range (1, 341):
    nums.append(i)
    
    



def check(num1, num2, num3, num4):
    if (
        (
            (num1) %3 != 0
        )and
        (
            (num2)%3 != 0
        )and
        (
            (num3)%3 !=0
        )and
        (
            (num4)%3 != 0
        )
        (
            (num1 + num2 + num3 + num4) == 129
        )
    ):return True
    return False






for i in range (len(nums) - 3):
    for j in range (i + 1, i + 2):
        for k in range (j + 1, j + 2):
            for p in range (k + 1, k + 2):
                if check(nums[i], nums[j], nums[k], nums[p]):
                    print('да')
                else:
                    print('нет')
                    

print('--------------------------')

                

nums = []
for i in range (1, 341):
    nums.append(i)
    
    



def check(num1, num2, num3, num4):
    if (
        (
            (num1) %3 != 0
        )and
        (
            (num2)%3 != 0
        )and
        (
            (num3)%3 !=0
        )and
        (
            (num4)%3 != 0
        )
        (
            (num1 + num2 + num3 + num4) == 226
        )
    ):return True
    return False





for max_sum in range (0, 227):
    for i in range (len(nums) - 3):
        for j in range (i + 1, i + 2):
            for k in range (j + 1, j + 2):
                for p in range (k + 1, k + 2):
                    if check(nums[i], nums[j], nums[k], nums[p]):
                        max_sum = max(max_sum, nums[i] + nums[j] + nums[k] + nums[p])



print(max_sum)
