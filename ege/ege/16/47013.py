def f(n):
    if n == 0: return 0
    if n%2 != 0: return f(n - 1) + 1
    if n > 0 and n%2 != 0: return f(n/2)

print(f(3))