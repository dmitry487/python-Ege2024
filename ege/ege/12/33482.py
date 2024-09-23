s = 100 * '1'

while '111' in s:
    s = s.replace('111', '22')
    s = s.replace('222', '11')
print(s)