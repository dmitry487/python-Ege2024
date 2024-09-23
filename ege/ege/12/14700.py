s = 7 * '1' + 7 * '2'
while '111' in s or '222' in s:
    if '111' in s:
        s = s.replace ('111', '2', 1)
    if '222' in s:
        s = s.replace ('222', '1', 1)
    
print(s)