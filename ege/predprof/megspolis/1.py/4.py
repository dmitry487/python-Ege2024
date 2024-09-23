counter = 0
counter1 = 0
for a in range (100, 1000):
    a_str = str(a)
    s = int(a_str[0]) + int(a_str[1]) + int(a_str[2])
    if a * s == 1105:
        print(a)
        counter += 1

if counter == 0:
    print('net')
    

print('---------------------')

for a in range (100, 1000):
    a_str = str(a)
    s = int(a_str[0]) + int(a_str[1]) + int(a_str[2])
    if a * s == 1106:
        print(a)
        counter1 += 1

if counter1 == 0:
    print('net')


print('--------------------')

for a in range (100, 1000):
    a_str = str(a)
    s = int(a_str[0]) + int(a_str[1]) + int(a_str[2])
    if a * s > 1503 and a * s < 1550:
        print(a * s)
        print(a)