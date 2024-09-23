from collections import Counter
f = open('ege3/24/55611/24-9.txt')


def check(row):
    spisok_True = ''
    res = ''
    for i in range (0, len(row) - 1):
        if row[i] == 'A':
            spisok_True += (row[i + 1])

    max_counter = Counter(spisok_True).most_common(1)[0][1]
    for letter in set(spisok_True):
        if spisok_True.count(letter) == max_counter:
            res += letter

    return res

spisok_vsego = ''
for i in f:
    spisok_vsego += check(i)


print(Counter(spisok_vsego).most_common(1))


