from fnmatch import fnmatch


for num in range (273, 10 ** 8 + 1, 273):
    if fnmatch(str(num), "12??36*1"):
        print(num, num//273)