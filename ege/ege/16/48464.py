import sys
sys.setrecursionlimit(500000000)

kolichestvo = 0
def f(n):
    if n == 0:return 0
    if n == n:return f(n - 1) + n
    
for n in range (765432010, 1542613234):
    if f(n)%3 != 0:
        kolichestvo += 1

print(kolichestvo)