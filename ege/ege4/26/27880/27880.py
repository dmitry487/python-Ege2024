f = open('ege4/26/27880/27880.txt')


items = [int(i) for i in f]
items = sorted(items)
sv_mesto = 8358
counter = 0
res = []
for item in items:
    if sv_mesto >= item:

        counter += 1


        sv_mesto -= item
        res.append(item)



print(items[::-1])
print(max(res))
print(sv_mesto)
print(counter)     

    
#611 27