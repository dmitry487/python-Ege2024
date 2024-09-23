from fnmatch import fnmatch


for num in range(317, 10**8 + 1, 317):
    if fnmatch(str(num), "12??1*56"):
        print(num, num//317)