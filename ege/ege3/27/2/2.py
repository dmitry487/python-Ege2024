lst = open("ege3/27/2/2.txt").read().splitlines()[1:]
lst = list(map(int, lst))
count26 = 0
countnot26 = 0
count31_not2 = 0
count2_not31 = 0
for x in lst:
    if x % 26 == 0:
        count26 += 1
    if x % 26 != 0:
        countnot26 += 1
    if x % 13 == 0 and x % 2 != 0:
        count31_not2 += 1
    if x % 13 != 0 and x % 2 == 0:
        count2_not31 += 1
print(count26 * countnot26 + count31_not2 * count2_not31 + count26 * (count26 - 1) // 2)


#19 199360639