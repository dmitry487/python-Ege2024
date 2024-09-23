from itertools import combinations

def p(x):
    return 5 <= x <= 40

def q(x):
    return 41<= x <= 54

def r(x):
    return 6 <= x <= 53

def a(x, start, stop):
    return start <= x <= stop

spisok_mnoj = combinations(sorted([5,40,41,54,6,53]), 2)

dlini = []

for start, stop in spisok_mnoj:
    flag = True

    for x in range (-5, 64):
        if not(
            ((not(p(x))) <= (q(x))) and\
            (r(x)) and (a(x, start, stop))
        ): flag = False

    if flag:
        dlini.append(stop - start)

print(dlini)
