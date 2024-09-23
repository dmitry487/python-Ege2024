from fnmatch import fnmatch


for num in range (2023, 10**10 + 1, 2023):
    if fnmatch(str(num), "1?2139*4"):
        print(num, num//2023)