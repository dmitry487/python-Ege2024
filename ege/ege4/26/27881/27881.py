f = open('ege4/26/27881/27881.txt')


items = [int(i) for i in f]
items = sorted(items)
res = []
sv_mesto = 1987
counter = 0

for item in items:
    if sv_mesto >= item:
        counter += 1

        sv_mesto -= item
        res.append(item)

print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)

#397 17
