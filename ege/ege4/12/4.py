for x in range (50):
    for y in range (50):
        for z in range (50):
            s = '0' + '1' * x + '2' * y + '3' * z

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)



            