f = open('ege4/26/27882/27882.txt')

items = [int(i) for i in f]

items = sorted(items)
res = []
counter = 0
sv_mesto = 1405

for item in items:
    if sv_mesto >= item:
        counter += 1


        sv_mesto -= item
        res.append(item)



print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)

#369, 9