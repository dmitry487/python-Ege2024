from itertools import combinations

def del_(n, m):
    return n%m == 0

def b(x):
    return 50 <= x <= 70

for a in range (1, 300):
    flag = True

    for x in range (1, 300):
        if not(
            del_(x, a) or ((del_(x, 23)) <= (not(b(x))))
        ):flag = False

    if flag:
        print(a)