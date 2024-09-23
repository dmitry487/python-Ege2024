f = open('ege3/26/13292/26_13292.txt')

n = 1000
k = 792

nums = [int(i) for i in f]

nums = sorted(nums)

nums = nums[:k]

last = nums[-1]

left_chet = []
right_nechet = []

for detali in nums:
    if detali%2 == 0:
        left_chet.append(detali)
    else:
        right_nechet.append(detali)

right_nechet = right_nechet[::-1]


obsh = left_chet + right_nechet

print('poslednyaya detal =', obsh.index(last) + 1)



print(sum(right_nechet[right_nechet.index(last) + 1:]))