s = '1' * 8 + '2' * 8
while '111' in s or '222' in s:
    if '111' in s:
        s = s.replace('111', '2', 1)
    if '222' in s:
        s = s.replace('222', '1', 1)
    
print(s)