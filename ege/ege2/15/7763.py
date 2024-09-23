from itertools import combinations

def p(x):
    return 5 <= x <= 30
def q(x):
    return 14 <= x <= 23
def a(x, start , stop):
    return start < x < stop

diapz = combinations(
    sorted([5, 30, 14 , 23]), 2
)

dlini = []
for start, stop in diapz:
    flag = True
    for x in range (100):
        if not(
            ((p(x)) == (q(x))) <=\
            (not(a(x, start , stop)))
        ):flag = False

    if flag:
        dlini.append(stop - start)

print(dlini)
print(max(dlini))
