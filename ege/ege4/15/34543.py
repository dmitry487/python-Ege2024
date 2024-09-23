from itertools import combinations


def p(x):
    return 3 <= x <= 13


def q(x):
    return 12 <= x <= 22

def a(x, start, stop):
    return start < x < stop



diapaz = combinations(
    sorted([3, 13, 12, 22]), 2
)

dlini = []
for start, stop in diapaz:
    flag = True

    for x in range (300):
        if not(
            ((a(x, start, stop)) <= (p(x))) or (q(x))
        ):flag = False


    if flag:
        dlini.append(stop - start)



print(dlini)
print(max(dlini))