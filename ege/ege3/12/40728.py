

for i in range (200, 300):
    s = '1' * i

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)



    print(s.count('1'), i)