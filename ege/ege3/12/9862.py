s = '1' * 128


while '333' in s or '11' in s:
    if '333' in s:
        s = s.replace('333', '1', 1)

    else:
        s = s.replace('11', '3', 1)


print(s)