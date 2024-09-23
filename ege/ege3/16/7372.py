def f(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) * n


print(f(6))