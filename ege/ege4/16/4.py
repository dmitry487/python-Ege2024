import sys
sys.setrecursionlimit(5000)
def f(n):
    if n >= 2024: return 1
    return f(n + 2) + f(n + 4)

res = set()
for n in range (1, 100):
    if f(n):
        res.add(n)


print(len(res))