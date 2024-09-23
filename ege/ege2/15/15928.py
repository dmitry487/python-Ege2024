from itertools import combinations


def a(x, start, stop):
    return start < x < stop

def a(y, start, stop):
    return start < y < stop

diapaz = combinations(
    sorted([-9, 9, -6, 6]), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for y in range (100):
        for x in range (100):
            if not(
                ((a(x, start, stop)) <= (x ** 2 <= 81)) and ((y ** 2 <= 36) <= (a(y, start, stop)))
            ):flag = False

    if flag:
        dlini.append(stop - start)

print(dlini)
print(max(dlini))