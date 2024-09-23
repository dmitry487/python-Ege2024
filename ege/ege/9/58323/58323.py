f = open('ege/9/58323/58323.txt')

nums = [[float (i) for i in row.split()] for row in f]

print(nums)