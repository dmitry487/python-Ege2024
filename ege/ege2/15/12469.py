from itertools import combinations


def d(x):
    return 7 <= x <= 68

def c(x):
    return 29 <= x <= 100


def a(x, start , stop):
    return start <= x <= x


dapaz = combinations(
    sorted([7, 68, 29, 100]), 2
)


dlini = []


for start, stop in dapaz:
    flag = True


    for x in range (100):
        if not(
            (d(x)) <= (((((not(c(x)))) and (not(a(x, start, stop))))) <= (not(d(x))))
        ):flag = False

    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))