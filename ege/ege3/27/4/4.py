# Считываю файл и получаю матрицу из двух столбцов
lines = open("ege3/27/4/27-A-2.txt").read().splitlines()[1:]
data = []
for line in lines:
    data.append(list(map(int, line.split())))

import itertools

lst = []  # Массив найденных сумм, удовлетворяющих условию
for item in itertools.product([False, True], repeat=len(data)):
    s = 0  # сумма чисел
    count_nc = 0  # количество нечетных чисел
    count_c = 0  # количество четных чисел
    for i in range(len(item)):
        if item[i]:
            d = data[i][0]
        else:
            d = data[i][1]
        s += d
        if d % 2 == 0:
            count_c += 1
        else:
            count_nc += 1
    if count_c > count_nc and s % 2 == 0:
        lst.append(s)
    if count_c < count_nc and s % 2 != 0:
        lst.append(s)
print(max(lst))
