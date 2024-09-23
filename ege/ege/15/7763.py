from itertools import combinations


def p(x):
    return 5<= x<= 30

def q(x):
    return 14 <= x <= 23

def a(x, start, stop):
    return start < x < stop
diapaz = combinations(
    (sorted([5,20,14,23])), 2
)


dlini = []
for start, stop in diapaz:
    flag = True
    for x in range (100):

        if not(
            ((p(x)) == (q(x))) <= (not(a(x, start, stop)))
        ):flag = True

    if flag:
        dlini.append(stop - start)

print(dlini)
print(max(dlini))
        
