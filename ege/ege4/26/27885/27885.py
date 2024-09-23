f = open('ege4/26/27885/27885.txt')


items = [int(i) for i in f]
items = sorted(items)

couter = 0
sv_mesto = 7718
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



#650 27