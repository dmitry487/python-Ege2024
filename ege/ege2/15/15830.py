def a(x, start, stop):
    return start <= x <= stop
diapaz = [1, 100]
diapaz = sorted(diapaz), 2
dlini = []
for start, stop in diapaz:
    flag = True
    for x in range (100):
        if not(
            ((a(x, start, stop)) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (a(x, start, stop)))
        ):flag = False

    if flag:
        dlini.append(stop - start)

print(dlini)