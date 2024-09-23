import sys
sys.setrecursionlimit(10000)

def f(n):
    if (n == 0): return 0
    if (n%3 == 0) and n > 0: return f(n / 3)
    if (n%3 > 0): return n%3 + f(n - n%3)

for n in range (1000):
    if f(n) == 11:
        print(n)
        break