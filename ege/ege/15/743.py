from itertools import combinations


spisok = []

for i in range (1, 9):
    diapaz = combinations(([1, 3, 5, 7, 9, 11, 6, 12]), i)
    spisok += (list(diapaz))


for a in spisok:
    flag = True

    for x in range (1, 15):
        if not(
            (x in {1, 3, 5, 7, 9, 11}) <=
            (x not in {3, 6, 9, 12}) or 
            (x in a)
        ): flag = False
    
    if flag:
        print(sum(a))
        break
    

    
    
