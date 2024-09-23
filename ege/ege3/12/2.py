max_sum = 0
for n in range (3, 10000):
    s = '7' + n * '1'


    while '1111' in s or '7777' in s:
        if '1111' in s:
            s = s.replace('1111', '77', 1)

        else:

            s = s.replace('7777', '11', 1)


    max_sum = max(max_sum, sum([int(i) for i in s]))



print(max_sum)

