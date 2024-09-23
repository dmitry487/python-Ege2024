f = open('ege4/26/27888/27888.txt')


items = [int(i) for i in f]

counter = 0
res = []
items = sorted(items)
sv_mesto = 9691


for item in sorted(items):
    if sv_mesto >= item:
        counter += 1

        sv_mesto -= item
        res.append(item)



print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)


#601 34