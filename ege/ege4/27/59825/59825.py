f = open('ege4/27/59825/27-A-6.txt')

nums = [int(i) for i in f]
max_sum = 0 

k = 81
res = []
for i in range (len(nums) - 1):
    for j in range (i + k, len(nums)):
        max_sum = sum(sorted(nums[i:j + 1])[-3:])
        rast = j - i
        res.append([max_sum, rast])


print(max(res))

