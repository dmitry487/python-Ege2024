from itertools import combinations

def del_(n,m):
    return n%m == 0

def p(x):
    return 5 <= x <= 137

def a(x, start, stop):
    return start <= x <= stop

diapaz = combinations(
    (
        sorted(
            [5,137]
        )
    ), 2
)

for start, stop in diapaz:
    flag = True


    for x in range (1, 100):
        if not(
            ((del_(x, 115)) and\
            (not(del_(x, 5)))) or\
            (
                (del_(a,x) <= (not(a, 5))) and\
                (not(a(p)))
            )
        ):flag = False

    if flag:
        print(a)
        break
