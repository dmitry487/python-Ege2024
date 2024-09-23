f = open('ege2/24/58329/24_58329.txt').read()


nums = [int(i) for i in f]

kolichestvo = 0
max_len = 0
for i in range (len(nums) - 2):
    if (nums[i] + nums[i + 1]) > nums[i + 2]:
        kolichestvo += 1
    else:
        max_len = max(max_len, kolichestvo + 2)
        kolichestvo = 0



print(max_len)