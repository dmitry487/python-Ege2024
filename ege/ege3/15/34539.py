from itertools import combinations


def p(x):
    return 22 <= x <= 72


def q(x):
    return 42 <= x <= 102


def a(x, start, stop):
    return start <= x <= stop


diapaz = combinations(
    sorted([22, 72, 42, 102]), 2
)


dlini = []
for start, stop in diapaz:
    flag = True


    for x in range (300):
        if not(
            not(not(a(x, start, stop)) and (p(x))) or (q(x))
        ):flag = False

    if flag:
        dlini.append(stop - start)



print(dlini)
print(min(dlini))