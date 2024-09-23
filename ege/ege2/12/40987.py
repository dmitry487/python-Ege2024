min_ = 1000
counter = 0
for n in range(200, 1000):
    s = '1' * n
    while ('1111' in s) or ('222' in s):
        if '1111' in s:
            s = s.replace('1111', '22', 1)
        else:
            s = s.replace('222', '1', 1)
    if min_ > s.count('1'):
        min_ = s.count('1')
        counter = n
print(counter)