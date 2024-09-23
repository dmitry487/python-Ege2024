f = open('ege4/26/27883/27883.txt')


items = [int(i) for i in f]
items = sorted(items)
sv_mesto = 543
counter = 0
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


