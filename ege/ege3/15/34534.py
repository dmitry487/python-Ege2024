from itertools import combinations


def p(x):
    return 2 <= x <= 10

def q(x):
    return 6 <= x <= 14


def a(x, start, stop):
    return start < x < stop


diapaz = combinations(
    sorted([2, 10, 6, 14]), 2
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