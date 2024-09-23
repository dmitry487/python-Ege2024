f = open('ege4/26/27887/27887.txt')


items = [int(i) for i in f]
items = sorted(items)
sv_mesto = 6021
res = []
counter = 0


for item in sorted(items):
    if sv_mesto >= item:
        counter += 1

        sv_mesto -= item
        res.append(item)



print(items[::-1])
print(max(res))
print(counter)
print(sv_mesto)

#459 45

