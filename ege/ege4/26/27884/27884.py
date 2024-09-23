f = open('ege4/26/27884/27884.txt')


items = [int(i) for i in f]
items = sorted(items)

sv_mesto = 8460
couter = 0
res = []


for item in items:
    if sv_mesto >= item:
        couter += 1

        sv_mesto -= item
        res.append(item)



print(items[::-1])
print(max(res))
print(couter)
print(sv_mesto)


#813 35