from itertools import combinations


def p(x):
    return 12 <= x <= 62


def q(x):
    return 52 <= x <= 92

def a(x, start , stop):
    return start <= x <= stop

diapaz = combinations(
    sorted([12, 62, 52, 92]), 2
)

dlini = []

for start , stop in diapaz:
    flag = True


    for x in range (100):
        if not(
            not(not(a(x, start, stop)) and (p(x))) or\
            (q(x))

        ): flag = False

    if flag:
        dlini.append(stop - start)


print(dlini)
