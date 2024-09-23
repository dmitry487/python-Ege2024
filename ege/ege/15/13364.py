from itertools import combinations

def p(x):
    return 130 <= x <= 171

def q(x):
    return 150 <= x<= 185

def a(x, start, stop):
    return start <= x <= stop

diapaz = combinations(
    (
        sorted(
            [130, 171, 150, 185]
        )
    ), 2
)

dlini = []

for start, stop in diapaz:
    flag = True

    for x in range (100, 200):
        if not(
            (p(x)) <=
            (
                (
                    (q(x)) and (not(a(x, start, stop))) 
                ) <=
                (
                    not(p(x))
                )
            )
        ): flag = False

    if flag:
        dlini.append(stop - start)

    
print(dlini)
print(min(dlini))