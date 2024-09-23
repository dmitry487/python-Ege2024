import sys
sys.setrecursionlimit(5000)

def f(n):
    if n<11: return 10
    return n + f(n - 1)
print (f(2022) - f(2019))