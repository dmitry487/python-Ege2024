from fnmatch import fnmatch 


for num in range (42, 10 ** 10 + 1, 42):
    if fnmatch(str(num), '48*15*0'):
        print(num, num//42)