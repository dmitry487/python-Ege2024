from itertools import combinations

def p(x):
    return 10 <= x <= 20

def q(x):
    return 35 <= x <= 45

def a(x, start, stop):
    return start <= x <= stop

spisok_mnoj = combinations(sorted([10, 20, 35, 45]), 2)

dlini = []

for start, stop in spisok_mnoj:
    flag = True
    
    for x in range (1, 70):
        if (not(p(x)) <= (q(x))) and\
              (not(a(x, start, stop))):flag = False

        
        if flag:
            dlini.append(stop - start)

print(dlini)
print(dlini.count(35))
