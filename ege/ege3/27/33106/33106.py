f = open('ege3/27/33106/inf_22_10_20_27b.txt')
s = f.readlines()
n = int(s[0])
sum = 0
dif1 = 20001
dif2 = 20001
dif3 = 20001
dif4 = 20001
for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    if x > y: sum += y
    else: sum += x
    if (abs(x-y) % 3 == 1) and (abs(x-y) < dif1):
        dif2 = dif1
        dif1 = abs(x - y)
    elif (abs(x-y) % 3 == 1) and (abs(x-y) < dif2): dif2 = abs(x-y)
    elif (abs(x-y) % 3 == 2) and (abs(x-y) < dif3):
        dif4 = dif3
        dif3 = abs(x - y)
    elif (abs(x-y) % 3 == 2) and (abs(x-y) < dif4): dif4 = abs(x-y)
if sum % 3 == 0:
    print(sum)
elif sum % 3 == 1:
    if (sum + dif3) < (sum + dif1 + dif2):
        print(sum + dif3)
    else: print(sum + dif1 + dif2)
elif sum % 3 == 2:
    if ((sum + dif1) < (sum + dif3 + dif4)):
        print(sum + dif1)
    else:
        print(sum + dif3 + dif4)


