from itertools import combinations

def b(x):
    return  24 <= x <= 90


def c(x):
    return 47 <= x <= 115

def a(x, start, stop):
    return start <= x <= stop


diapaz = combinations(
    sorted([24, 90, 47, 115]), 2
)

dlini = []


for start, stop in diapaz:
    flag = True

    for x in range (1, 1000):
        if not(
            (c(x)) <= (((not(a(x, start, stop))) and (b(x))) <= (not(c(x))))
        ):flag = False


    if flag:
        dlini.append(stop - start)



print(dlini)
print(min(dlini))