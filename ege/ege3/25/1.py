from fnmatch import fnmatch


for num in range (48181, 10 ** 11, 48181):
    if fnmatch(str(num), "5?754*86"):
        print(num, num//48181)