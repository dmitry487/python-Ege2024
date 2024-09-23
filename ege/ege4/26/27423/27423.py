f = open('ege4/26/27423/26_demo.txt')

items = [int(i) for i in f]
items = sorted(items)
sv_mesto = 8200
counter = 0
res = []
for item in items:
    if sv_mesto >= item:
        counter += 1

        sv_mesto -= item
        res.append(item)


print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)


