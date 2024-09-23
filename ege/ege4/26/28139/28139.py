f = open('ege4/26/28139/28139.txt')


items = [int(i) for i in f]
sv_mesto = 731
counter = 0
items = sorted(items)
res = []


for item in items:
    if sv_mesto >= item:
        sv_mesto -= item
        res.append(item)

        counter += 1


print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)