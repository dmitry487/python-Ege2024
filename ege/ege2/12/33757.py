def alg(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '101', 1)
        s= s.replace('03', '202', 1)
    return s

for q1 in range(60):
    for q2 in range(60):
        for q3 in range (60):
            s = '0' + q1 * '1' + q2 * '2' + q3 * '3' + '0'

            s = alg(s)

            if s.count('1') == 20 and s.count('2') == 10 and s.count('3') == 70:
                print(q1)