from itertools import combinations


def p(x):
    return 17 <= x <= 54

def q(x):
    return 37 <= x <= 83


def a(x, start, stop):
    return  start <= x <= stop

diapaz = combinations(
    sorted([17, 54, 37, 83]), 2
)

dlini = []
for start, stop in diapaz:
    flag = True

    for x in range (100):
        if not(
            (p(x)) <= (((q(x)) and not(a(x, start, stop))) <= (not(p(x))))
        ):flag = False

    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))