from itertools import combinations

def p(x):
    return 4 <= x <= 15


def q(x):
    return 12 <= x <= 20


def a(x, start, stop):
    return start <= x <= stop

diapaz = combinations(
    sorted([4, 15, 12, 20]), 2
)


dlini = []


for start, stop in diapaz:
    flag = True


    for x in range (1, 200):
        if not( 
            (p(x) and q(x)) <= (a(x, start, stop))
        ): flag = False


    if flag:
        dlini.append(stop - start)



print(dlini)
print(min(dlini))