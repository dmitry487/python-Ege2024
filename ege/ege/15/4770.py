from itertools import combinations

def p(x):
    return 35 <= x <= 55

def q(x):
    return 45 <= x <= 65

def a(x, start, stop):
    return start <= x <= stop

diapaz = combinations(
    sorted(
        [35, 55, 45, 65]
    ), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for x in range (20, 75):
        if not(
            ((p(x)) <= (a(x, start, stop))) and ((not(a(x, start, stop))) <= (not(q(x))))
        ): flag = False
    
    if flag:
        dlini.append(stop - start)

print(dlini)
print(min(dlini))