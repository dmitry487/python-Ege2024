kolichestvo = 1
max_ = -1
for n in range (1, 200):
    s = '1' * n

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
        max_ = max(max_, s.count('1'))
        kolichestvo += 1

        print(max_, kolichestvo)