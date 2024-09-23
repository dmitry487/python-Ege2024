for i in range (1, 100):
    for j in range (1, 100):
        for k in range (1, 100):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'

            while '00' not in s:
                s = s.replace ('01', '210' ,1)
                s = s.replace ('02', '3101', 1)
                s = s.replace ('03', '2012', 1)
            if i == 61 and j == 50 and k == 18:
                print(s)