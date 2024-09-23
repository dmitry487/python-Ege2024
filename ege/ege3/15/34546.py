from itertools import combinations

def p(x):
    return 23 <= x <= 58


def q(x):
    return 1 <= x <= 39


def a(x, start, stop):
    return start <= x <= stop


diapaz = combinations(
    sorted([23, 58, 1, 39]), 2
)

dlini = []
for start, stop in diapaz:
    flag = True


    for x in range (300):
        if not(
            ((p(x)) or (a(x, start, stop))) <= ((q(x)) or (a(x, start, stop)))
        ):flag = False


    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))