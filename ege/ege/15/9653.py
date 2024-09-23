from itertools import combinations

def p(x):
    return 10 <= x <= 29

def q(x):
    return 13 <= x <= 18

def a(x, start, stop):
    return start < x < stop

diapaz = combinations(
    sorted(
        [10, 29, 13, 18]
    ), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for x in range(0, 30):
        if not(
            (
                (a(x, start, stop) <= (p(x)))
            ) or 
            (
                q(x)
            )
        ): flag  = False

    if flag:
        dlini.append(stop - start)

print(dlini)
print(max(dlini))

    