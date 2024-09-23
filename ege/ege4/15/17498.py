from itertools import combinations

def d(x):
    return 17 <= x <= 58

def c(x):
    return 29 <= x <= 80


def a(x, start, stop):
    return start <= x <= stop


diapaz = combinations(
    sorted([17, 58, 29, 80]), 2
)

dlini = []


for start, stop in diapaz:
    flag = True

    for x in range (300):
        if not(
            (d(x)) <= ((not(c(x)) and (not(a(x,start, stop)))) <= (not(d(x))))
        ):flag = False


    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))