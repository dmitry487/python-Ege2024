from fnmatch import fnmatch

for num in range (9117, 10 ** 9 + 1, 9117):
    if fnmatch(str(num), '4*64*9?7'):
        print(num)