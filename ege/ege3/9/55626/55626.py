f = open('ege3/9/55626/55626.txt')



nums = [[int(i) for i in row.split()] for row in f]


def check(row):
    fl = True
    for num in nums:
        if not(nums.count(num) == 50):
            fl = False
        
    for num in row:
        if not(row.count(num) == 1):
            fl = False

    return fl

    
kolichestvo = 0



for row in nums:
    if check(row):
        kolichestvo += 1


print(kolichestvo)
