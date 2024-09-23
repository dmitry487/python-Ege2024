from itertools import combinations


def p(x):
    return 10 <= x <= 15

def q(x):
    return 10 <= x <= 20

def r(x):
    return 5 <= x <= 15

def a(x,start, stop):
    return start <= x <= stop

diapaz = combinations(
    sorted([10, 15, 10, 20, 5, 15]), 2
)

dlini = []


for start, stop in diapaz:
    flag = True


    for x in range (200):
        if (not(((a(x, start, stop)) <= (p(x))))) and (not(((q(x)) <= (r(x))))): flag = False


    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))