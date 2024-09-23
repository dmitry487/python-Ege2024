f = open('ege/5/13617.txt')

nums = [int(i) for i in f]


kolichestvo = 0
if '123' in nums:
    kolichestvo += 1
else:
    print('nihuya')
    print(kolichestvo)