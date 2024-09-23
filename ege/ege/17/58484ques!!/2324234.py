f = open('ege/17/58484/17-13.txt')

nums = [int(i) for i in f]

for num in sorted(nums):
    if abs(num) in range (100, 1000) and abs(num)%10 == 5:
        print(num)