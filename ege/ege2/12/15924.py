s = '1' * 101


while '1111' in s:
    s = s.replace('1111', '22', 1)
    s = s.replace('222', '11', 1)

print(s)