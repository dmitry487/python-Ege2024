f = open('ege4/26/27886/27886.txt')


items = [int(i) for i in f]
items = sorted(items)

sv_mesto = 5955
res = []
couter = 0

for item in items:
    if sv_mesto >= item:
        couter += 1

        sv_mesto -= item
        res.append(item)


print(items[::-1])
print(max(res))
print(couter)
print(sv_mesto)
    


#458 39