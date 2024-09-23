from itertools import combinations

def p(x):
    return 20 <= x <= 50

def q(x):
    return 30 <= x <= 65

def a(x, start, stop):
    return start <= x <= stop

diapaz = combinations(
    sorted(
        [20, 50, 30, 65]
    ), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for x in range (10, 75):
        if not(
            (not(a(x, start, stop))) <=
            (
                (p(x)) <= (not(q(x)))
            )
        ): flag = False

    if flag:
        dlini.append(stop - start)

    
print(dlini)
print(min(dlini))