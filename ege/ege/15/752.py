from itertools import combinations

spisok_mnoj = []
kolichestvo = 0
for i in range (1, 9):
    spisok_mnoj += list(combinations([3, 6, 9, 12, 1, 2, 4, 5], i))
    
for mnoj in spisok_mnoj:
    flag = True

    for x in range (1, 30):
        if not(
            not(not(x in mnoj) and (x in {3, 6, 9, 12})) or\
            not(x in {1, 2, 3, 4, 5, 6})
        ): flag = False

    if flag:
        kolichestvo += 1
        break

print(mnoj)

