from fnmatch import fnmatch


for num in range (4891, 10 ** 10 + 1, 4891):
    if fnmatch(str(num), '1?2711*0'):
        print(num)