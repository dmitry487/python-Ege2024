s = 200 * '1'
min_ = 2000000
while '1111' in s:
    s = s.replace ('1111', '22')
    s = s.replace ('222', '1')
    min_ = min(min_,s.count('1'))
    if min_ == s.count('1'):
        print(s)

    