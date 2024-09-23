from itertools import combinations

def p(x):
    return 25 <= x <= 50

def q(x):
    return 32 <= x <= 47

def a(x, start, stop):
    return start < x < stop

diapaz = combinations(
    sorted(
        [25, 32, 47, 50]
    ), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for x in range(0, 30):
        if not(
            (not(a(x, start, stop) <= (p(x))) <=\
             ((a(x, start, stop)) <= q(x)))
        ): flag = False

    if flag:
        dlini.append(stop - start)

print(dlini)
print(max(dlini))
