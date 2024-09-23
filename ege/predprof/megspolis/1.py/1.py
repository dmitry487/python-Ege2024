sin = []
red = []
res = []
for num in range (25):
    res.append(num)
    for i in range (10):
        sin.append(num)

    for i in range (40):
        red.append(num)


    if (sum(red) + sum(sin))%50 == 16 and (sum(red) + 2 * (sum(sin)) % 50 == 31,2):
        print(red)
        print(sin)



